from langchain_core.messages import HumanMessage, SystemMessage

def recommend_problem(llm, platform, level):
  system_prompt = """
    당신은 알고리즘 문제 추천 봇입니다."
    사용자가 플랫폼과 난이도를 주면, 해당 플랫폼의 난이도 범위에 맞는 랜덤 문제 하나를 추천하고,
    문제 이름, 링크, 난이도, 문제 설명을 제공하세요.
    여기서 "문제 설명"이란 입출력 조건과, 테스트 케스트 예시도 모두 포함합니다.
    출력에는 이외에 다른 텍스트나 마크다운을 포함하지 마세요.
    문제를 추천할 뿐, 푸는 방법이나 힌트를 알려주지 마세요.   
  """
  human_prompt = f"플랫폼: {platform}\n, 난이도: {level}\n이 조건에 맞는 문제를 랜덤으로 추천해주세요."
  messages = [SystemMessage(content = system_prompt), HumanMessage(content = human_prompt)]
  
  return llm.invoke(messages).content