#C:\Users\Mohini Ruhela\PycharmProjects\coding_ninjas\main.py
import streamlit as st
#from streamlit_chat message
from streamlit_chat import message
from bardapi import Bard
import json


#function to generate the output
token = 'YAgajtkgvcXtOUgpMG_dcdgj1I2gDANVsYqHYlLWh9_QUkWO_yxcwOGSK09uDInhM1oXVA.'
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response



#function to get user input the output
def get_text():
    input_text = st.text_input("Coding Ninjas-CN BOT:", "", key='input')
    return input_text

st.title('🤖Personal Tutoring Bot!')

#<div class="appview-container css-1wrcr25 e1g8pov66" data-testid="stAppViewContainer" data-layout="narrow"><section tabindex="0" class="main css-uf99v8 e1g8pov65"><div class="block-container css-1y4p8pa e1g8pov64" style="position: relative;"><div style="overflow: visible; width: 0px; display: flex; flex-direction: column; flex: 1 1 0%;"><div width="118" data-testid="stVerticalBlock" class="css-1tqk7cw esravye0"><div data-stale="false" width="118" class="element-container css-1vkolo9 esravye2"><div class="stMarkdown" style="width: 118px;"><div data-testid="stMarkdownContainer" class="css-nahz7x eqr7zpz4" style="width: 118px;"><div class="css-k7vsyb eqr7zpz1"><h1 id="personal-tutoring-bot"><div class="css-zt5igj eqr7zpz3"><a href="#personal-tutoring-bot" class="css-15zrgzn eqr7zpz2"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><span class="css-10trblm eqr7zpz0">personal tutoring bot</span></div></h1></div></div></div></div><div data-stale="false" width="118" class="element-container css-1vkolo9 esravye2"><div class="row-widget stTextInput css-1x38fev e1q7aese0" width="118"><label aria-hidden="true" class="css-k3w14i e1oyb3mv3"><div data-testid="stMarkdownContainer" class="css-q8sbsg eqr7zpz4"><p>Coding Ninjas-CN BOT:</p></div></label><div data-baseweb="input" class="st-bc st-b3 st-bd st-b8 st-be st-bf st-bg st-bh st-bi st-bj st-bk st-bl st-bm st-b1 st-bn st-au st-ax st-av st-aw st-ae st-af st-ag st-ah st-ai st-aj st-bo st-bp st-bq st-br st-bs st-bt st-bu"><div data-baseweb="base-input" class="st-b3 st-b8 st-bv st-b1 st-bn st-ae st-af st-ag st-ah st-ai st-aj st-bw st-bs"><input aria-label="Coding Ninjas-CN BOT:" aria-invalid="false" aria-required="false" autocomplete="" inputmode="text" name="" placeholder="" type="text" class="st-bc st-bx st-by st-bz st-c0 st-c1 st-c2 st-c3 st-c4 st-c5 st-c6 st-b8 st-c7 st-c8 st-c9 st-ca st-cb st-cc st-cd st-ce st-ae st-af st-ag st-cf st-ai st-aj st-bw st-cg st-ch st-ci" value=" enter your text "></div></div><div class="css-1if5ada e1oyb3mv1"></div></div></div></div></div><div class="resize-triggers"><div class="expand-trigger"><div style="width: 151px; height: 476px;"></div></div><div class="contract-trigger"></div></div></div><div data-iframe-height="true" class="css-1wrevtn e1g8pov60"></div><div class="css-qcqlej e1g8pov63"></div><footer class="css-cio0dv e1g8pov61">Made with <a href="//streamlit.io" target="_blank" class="css-z3au9t e1g8pov62">Streamlit</a></footer></section></div>
#url = 'https://images.unsplash.com/photo-1537420327992-d6e192287183?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3BhY2V8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=1000&q=60'
#new_url='https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=872&q=80'
#data-testid="stAppViewContainer"
changes = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1639152201720-5e536d254d81?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1032&q=80');
    background-size: cover;
}
  
</style>
'''

#class="element-container css-1hj1hs7 esravye2"
st.markdown(changes, unsafe_allow_html=True)
st.markdown('<link href="scratch.css" rel="stylesheet">', unsafe_allow_html=True)


print(st.session_state)
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []



#accepting user input
user_input = get_text()
if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_"+str(i), is_user=True)


prompt = input('write your text:')
response = generate_response(prompt)
print(response)

