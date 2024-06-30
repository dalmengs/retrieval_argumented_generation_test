import asyncio
import json
from tqdm import tqdm
from generated_data_check import list_files
from experiment_function import *
import vector_database

async def test1():
    file_list = list_files("./summary")

    print("Insert Data")
    idx = 1
    for file_name in tqdm(file_list, desc=f"[Retrieval Test]"):
        data = list(eval(open("./summary/{}".format(file_name), "r").read()))
        await vector_database.insert_data(
            file_id=file_name,
            func=aggregated_sentence_vector,
            args=[data]
        )
        idx += 1

    result = {
        "result": []
    }
    
    print("Retrieval Test")
    idx = 1
    total = 0
    total_succeed = 0
    for file_name in file_list:
        temp = {
            "file_name": file_name,
            "number_of_testcases": len(file_list),
            "test_result": [],
        }
        data = list(eval(open("./transcript/{}".format(file_name), "r").read()))
        succeed = 0
        for q in tqdm(data, desc=f"[Retrieval Test] Testcase #{idx}"):
            retrieval_file_name = await vector_database.retrieval(text=q)
            temp["test_result"].append({
                "retrieval_file_name": retrieval_file_name,
                "is_passed": file_name in retrieval_file_name
            })
            succeed += 1 if file_name in retrieval_file_name else 0
            total += 1
        total_succeed += succeed
        temp["succeed"] = succeed
        result["result"].append(temp)
        idx += 1
    
    result["total_test"] = total
    result["total_succeed"] = total_succeed
    
    f = open("./result/1.json", "w")
    f.write(json.dumps(result, indent=4))
    f.close()
    return result

async def test2():
    file_list = list_files("./summary")

    print("Insert Data")
    idx = 1
    for file_name in tqdm(file_list, desc=f"[Retrieval Test]"):
        data = list(eval(open("./summary/{}".format(file_name), "r").read()))
        await vector_database.insert_data(
            file_id=file_name,
            func=averaged_sentence_vector,
            args=[data]
        )
        idx += 1

    result = {
        "result": []
    }
    
    print("Retrieval Test")
    idx = 1
    total = 0
    total_succeed = 0
    for file_name in file_list:
        temp = {
            "file_name": file_name,
            "number_of_testcases": len(file_list),
            "test_result": [],
        }
        data = list(eval(open("./transcript/{}".format(file_name), "r").read()))
        succeed = 0
        for q in tqdm(data, desc=f"[Retrieval Test] Testcase #{idx}"):
            retrieval_file_name = await vector_database.retrieval(text=q)
            temp["test_result"].append({
                "retrieval_file_name": retrieval_file_name,
                "is_passed": file_name in retrieval_file_name
            })
            succeed += 1 if file_name in retrieval_file_name else 0
            total += 1
        total_succeed += succeed
        temp["succeed"] = succeed
        result["result"].append(temp)
        idx += 1
    
    result["total_test"] = total
    result["total_succeed"] = total_succeed
    
    f = open("./result/2.json", "w")
    f.write(json.dumps(result, indent=4))
    f.close()
    return result

async def test3():
    file_list = list_files("./summary")

    print("Insert Data")
    idx = 1
    for file_name in tqdm(file_list, desc=f"[Retrieval Test]"):
        data = list(eval(open("./summary/{}".format(file_name), "r").read()))
        await vector_database.insert_data(
            file_id=file_name,
            func=weighted_sentence_vector,
            args=[open("./chat/{}".format(file_name), "r").read(), data]
        )
        idx += 1

    result = {
        "result": []
    }
    
    print("Retrieval Test")
    idx = 1
    total = 0
    total_succeed = 0
    for file_name in file_list:
        temp = {
            "file_name": file_name,
            "number_of_testcases": len(file_list),
            "test_result": [],
        }
        data = list(eval(open("./transcript/{}".format(file_name), "r").read()))
        succeed = 0
        for q in tqdm(data, desc=f"[Retrieval Test] Testcase #{idx}"):
            retrieval_file_name = await vector_database.retrieval(text=q)
            temp["test_result"].append({
                "retrieval_file_name": retrieval_file_name,
                "is_passed": file_name in retrieval_file_name
            })
            succeed += 1 if file_name in retrieval_file_name else 0
            total += 1
        total_succeed += succeed
        temp["succeed"] = succeed
        result["result"].append(temp)
        idx += 1
    
    result["total_test"] = total
    result["total_succeed"] = total_succeed
    
    f = open("./result/3.json", "w")
    f.write(json.dumps(result, indent=4))
    f.close()
    return result

async def test4():
    file_list = list_files("./summary")

    print("Insert Data")
    idx = 1
    for file_name in tqdm(file_list, desc=f"[Retrieval Test]"):
        data = list(eval(open("./summary/{}".format(file_name), "r").read()))
        await vector_database.insert_data(
            file_id=file_name,
            func=model_choose_sentence_vector,
            args=[open("./chat/{}".format(file_name), "r").read(), data]
        )
        idx += 1

    result = {
        "result": []
    }
    
    print("Retrieval Test")
    idx = 1
    total = 0
    total_succeed = 0
    for file_name in file_list:
        temp = {
            "file_name": file_name,
            "number_of_testcases": len(file_list),
            "test_result": [],
        }
        data = list(eval(open("./transcript/{}".format(file_name), "r").read()))
        succeed = 0
        for q in tqdm(data, desc=f"[Retrieval Test] Testcase #{idx}"):
            retrieval_file_name = await vector_database.retrieval(text=q)
            temp["test_result"].append({
                "retrieval_file_name": retrieval_file_name,
                "is_passed": file_name in retrieval_file_name
            })
            succeed += 1 if file_name in retrieval_file_name else 0
            total += 1
        total_succeed += succeed
        temp["succeed"] = succeed
        result["result"].append(temp)
        idx += 1
    
    result["total_test"] = total
    result["total_succeed"] = total_succeed
    
    f = open("./result/4.json", "w")
    f.write(json.dumps(result, indent=4))
    f.close()
    return result

async def test5():
    file_list = list_files("./summary")

    print("Insert Data")
    idx = 1
    for file_name in tqdm(file_list, desc=f"[Retrieval Test]"):
        await vector_database.insert_data(
            file_id=file_name,
            func=conversation_vector,
            args=[open("./chat/{}".format(file_name), "r").read()]
        )
        idx += 1

    result = {
        "result": []
    }
    
    print("Retrieval Test")
    idx = 1
    total = 0
    total_succeed = 0
    for file_name in file_list:
        temp = {
            "file_name": file_name,
            "number_of_testcases": len(file_list),
            "test_result": [],
        }
        data = list(eval(open("./transcript/{}".format(file_name), "r").read()))
        succeed = 0
        for q in tqdm(data, desc=f"[Retrieval Test] Testcase #{idx}"):
            retrieval_file_names = await vector_database.retrieval(text=q)
            temp["test_result"].append({
                "retrieval_file_name": retrieval_file_names,
                "is_passed": file_name in retrieval_file_names
            })
            succeed += 1 if file_name in retrieval_file_names else 0
            total += 1
        total_succeed += succeed
        temp["succeed"] = succeed
        result["result"].append(temp)
        idx += 1
    
    result["total_test"] = total
    result["total_succeed"] = total_succeed
    
    f = open("./result/5.json", "w")
    f.write(json.dumps(result, indent=4))
    f.close()
    return result

async def test6():
    file_list = list_files("./summary")

    print("Insert Data")
    idx = 1
    for file_name in tqdm(file_list, desc=f"[Retrieval Test]"):
        await vector_database.insert_data(
            file_id=file_name,
            func=conversation_public_vector,
            args=[open("./chat/{}".format(file_name), "r").read()]
        )
        idx += 1

    result = {
        "result": []
    }
    
    print("Retrieval Test")
    idx = 1
    total = 0
    total_succeed = 0
    for file_name in file_list:
        temp = {
            "file_name": file_name,
            "number_of_testcases": len(file_list),
            "test_result": [],
        }
        data = list(eval(open("./transcript/{}".format(file_name), "r").read()))
        succeed = 0
        for q in tqdm(data, desc=f"[Retrieval Test] Testcase #{idx}"):
            retrieval_file_names = await vector_database.retrieval(text=q)
            temp["test_result"].append({
                "retrieval_file_name": retrieval_file_names,
                "is_passed": file_name in retrieval_file_names
            })
            succeed += 1 if file_name in retrieval_file_names else 0
            total += 1
        total_succeed += succeed
        temp["succeed"] = succeed
        result["result"].append(temp)
        idx += 1
    
    result["total_test"] = total
    result["total_succeed"] = total_succeed
    
    f = open("./result/6.json", "w")
    f.write(json.dumps(result, indent=4))
    f.close()
    return result

asyncio.run(test6())
