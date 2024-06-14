import os
import asyncio

def list_files(directory):
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            files.append(filename)
    return files

def check_file_exists(path):
    return os.path.isfile(path)

async def main():
    succeed, failed = [], []

    file_list = list_files("./chat")

    print("{}개의 대화 데이터가 있습니다.".format(len(file_list)))
    
    idx = 1
    for file_name in file_list:
        print("[파일 {} 테스트. '{}']".format(idx, file_name))
        idx += 1

        print("대화 데이터: ", end="")
        try:
            open("./chat/{}".format(file_name), "r").read()
        except Exception:
            print("대화 데이터 읽기 실패!")
            print("파일 '{}'을 확인하세요.".format(file_name))
            failed.append(file_name)
            continue
        print("테스트 성공!")

        print("요약 데이터: ", end="")
        try:
            open("./summary/{}".format(file_name), "r").read()
        except Exception:
            print("요약 데이터 읽기 실패!")
            print("파일 '{}'을 확인하세요.".format(file_name))
            failed.append(file_name)
            continue
        print("테스트 성공!")

        print("요약 데이터 파싱: ", end="")
        try:
            data = list(eval(open("./summary/{}".format(file_name), "r").read()))
            if not isinstance(data, list) or not len(data) == 3:
                raise Exception()
        except Exception as e:
            print("파싱 테스트 실패!")
            print("파일 '{}'을 확인하세요.".format(file_name))
            failed.append(file_name)
            continue
        print("테스트 성공!")

        print("발화 데이터 파싱: ", end="")
        try:
            data = list(eval(open("./transcript/{}".format(file_name), "r").read()))
            if not isinstance(data, list) or not len(data) == 10:
                raise Exception()
        except Exception as e:
            print("파싱 테스트 실패!")
            print("파일 '{}'을 확인하세요.".format(file_name))
            failed.append(file_name)
            continue
        print("테스트 성공!")

        succeed.append(file_name)
    
    print("[테스트 종료]")
    print("테스트 개수:", len(succeed) + len(failed))
    print("테스트 성공:", len(succeed))
    print("테스트 실패:", len(failed))
    if len(failed):
        print("실패 테스트 목록:", failed)
    
asyncio.run(main())