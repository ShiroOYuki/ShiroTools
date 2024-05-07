def check_short_answer(user_ans:str, true_ans:str):
    return user_ans == true_ans

def check_single_choice(user_ans:str, true_ans:str):
    return user_ans == true_ans

def check_multiple_choice(user_ans:str, true_ans:str):
    
    return "".join(sorted(user_ans.split(","))) == "".join(sorted(true_ans)), sorted(user_ans.split(","))