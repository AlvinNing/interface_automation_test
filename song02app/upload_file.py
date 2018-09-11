from django.http import HttpResponse
import requests
import xlrd
import time
from xlutils import copy
from song02app import models


class logic():

    def upload_file(self, request):
        if request.method == "POST":
            File = request.FILES.get('files', None)
            if File is None:
                return HttpResponse('请上传需要执行自动化测试的文件')
            else:
                with open("./song02app/testFile/%s" % File.name, 'wb+') as f:
                    for chunk in File.chunks():
                        f.write(chunk)

    def readExcel(self, file_path):
        try:
            book = xlrd.open_workbook(file_path)
        except Exception as e:
            print("读取文件不存在！请检查文件及路径是否正确！"+e)
            return e
        else:
            sheet = book.sheet_by_index(0)
            rows = sheet.nrows  # 取这个sheet的总行数
            case_list = []
            for i in range(rows):
                if i != 0:
                    # 把每行的用例添加到case_list中
                    case_list.append(sheet.row_values(i))
        return case_list

    def interfaceTest(self, case_list, file_path):
        test_res = []
        request_urls = []
        responses = []
        for case in case_list:
            try:
                product = case[0]
                case_id = case[1]
                interface_name = case[2]
                case_detail = case[3]
                method = case[4]
                url = case[5]
                param = case[6]
                res_check = case[7]
                people = case[10]
                remarks = case[12]
                print('…………………………'+'try')
                print('备注'+remarks)
                # 将Excel中内容读取后写入sqlite3数据库保存
                models.result.objects.create(project=product, case_id=case_id, interface_name=interface_name, case_description=case_detail,
                req_method=method, req_url=url, req_parameter=param, checkpoint=res_check, people=people, remarks=remarks)
                # s = models.result.objects.all()
                # for i in len(s):
                #     print(s[i])
            except Exception as e:
                print("测试用例格式不正确,请检查接口测试用例格式！%s" % e)
                print('…………………………'+'exception')
                return "测试用例格式不正确,请检查接口测试用例格式！%s" % e
            if param == '':
                request_urls.append(url)
            else:
                lo = logic()
                new_url = url+'?'+lo.urlParam(param)
                request_urls.append(new_url)
            if method.upper() == 'GET':
                results = requests.get(new_url).text
                responses.append(results[0:100]+'……')
                lo = logic()
                res = lo.readRes(results, res_check)
            else:
                results = requests.post(new_url).text
                responses.append(results[0:100]+'……')
                lo = logic()
                res = lo.readRes(results, res_check)
            if 'pass' in res:
                test_res.append('pass')
            else:
                test_res.append('fail')
            models.result.objects.create(response_message=responses, test_res=test_res)
            l = logic()
            l.copy_excel(file_path, test_res, responses)

    def readRes(res, res_check):
        res = res.replace('":"', "=").replace('":"', "=")
        res_check =res_check.split(';')
        for s in res_check:
            if s in res:
                pass
            else:
                return '错误，返回参数和预期结果不一致'+str(s)
        return 'pass'

    def urlParam(self, param):
        return param.replace(';', '&')

    def copy_excel(self, file_path, res_flags, responses):
        book = xlrd.open_workbook(file_path)
        new_book = copy.copy(book)
        sheet = new_book.get_sheet(0)
        i = 1
        for request_urls, responses, flag in zip(responses, res_flags):
            sheet.write(i, 9, u'%s' % responses)
            sheet.write(i, 11, u'%s' % flag)
            i = i + 1
        new_book.save('./song02app/testFile/%s_测试结果.xls' % time.strftime('%Y%m%d%H%M%S'))

