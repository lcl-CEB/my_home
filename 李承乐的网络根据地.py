'''我的主页'''
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import time

page = st.sidebar.radio('首页', ['网页介绍', '图片处理工具', '图片分享与绘制', '额外功能——词典', '留言区', '问答(一定要看看！)', '入网必看！！！'])

def page_1():
    warning()
    st.balloons()
    with open('霞光.mp3', 'rb') as f:
        shadow = f.read()
    st.audio(shadow)
    st.divider()
    st.title('这里是首页')
    st.write(':blue[你好！！！！！]')
    st.write(':blue[！！！！！好你]')
    st.write(':blue[你好！！！！！]')
    st.write(':blue[！！！！！好你]')
    st.write(':blue[你好！！！！！]')
    st.write(':blue[！！！！！好你]')
    st.write(':blue[你好！！！！！]')
    st.write(':blue[！！！！！好你]')
    st.write(':blue[你好！！！！！]')
    st.divider()
    st.subheader(':green[网站介绍：请访问 {180.101.50.188} ]')
    
def page_2():
    warning()
    tab1, tab2 = st.tabs(['图片换色工具', '敬请期待'])
    with tab1:
        uploaded_file = st.file_uploader('(上传图片……)',type=['jpg', 'png', 'jpeg'])
        st.divider()
        if uploaded_file:
            file_name = uploaded_file.name
            file_type = uploaded_file.type
            file_size = uploaded_file.size
            img = Image.open(file_name)
            st.subheader('这是你选择的图片：')
            st.image(img)
            pic_choose = st.select_slider('请选择换色方式', ['r, g, b', 'r, b, g', 'b, r, g', 'b, g, r', 'g, r, b', 'g, b, r'])
            pic_choose = pic_choose.split(', ')
            for i in range(3):
                if (pic_choose[i] == "r"):
                    pic_choose[i] = 0
                elif (pic_choose[i] == "g"):
                    pic_choose[i] = 1
                elif (pic_choose[i] == "b"):
                    pic_choose[i] = 2
            change_img = img_change(img, pic_choose)
            st.image(change_img)
            download = st.button(label='下载换色后的图片')
            if download:
                change_img.save('new_pic.png')
                st.write('已保存为‘new_pic.png’')
    with tab2:
        st.warning('510 Not Extended')
        
def page_3():
    warning()
    st.image(Image.open('pic.png'))
    tab1, tab2 = st.tabs(['绘制图片（俗称画画）', '图片分享'])
    with tab1:
        canvas = st_canvas(width=700,height=800,stroke_width=3)
        drawing = Image.fromarray(canvas.image_data)
        download = st.button(label='下载绘画作品') 
        if download:
            drawing.save('my_drawing.png')
            st.write('已保存为‘my_drawing.png’')
    with tab2:
        st.warning('451 Unavailable For Legal Reasons')

def page_4():
    warning()
    st.header('大聪明词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('查询的单词？')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''# 恭喜你触发彩蛋！''')
    elif word not in words_dict and word:
        st.error('404 Not Found')
        
def page_5():
    try:
        st.write('留言区')
        with open('leave_messages.txt', 'r', encoding='utf-8') as f:
            messages_list = f.read().split('\n')
        for i in range(len(messages_list)):
            messages_list[i] = messages_list[i].split('#')
        for i in messages_list:
            if i[1] == '杨瑾诚':
                with st.chat_message('🌞'):
                    st.write(i[1],':',i[2])
            elif i[1] == '李致远':
                with st.chat_message('🍥'):
                    st.write(i[1],':',i[2])
        name = st.selectbox('我是……', ['杨瑾诚', '李致远'])
        new_message = st.text_input('想要说的话……')
        if st.button('留言'):
            messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
            with open('leave_messages.txt', 'w', encoding='utf-8') as f:
                message = ''
                for i in messages_list:
                    message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
                message = message[:-1]
                f.write(message)
    except:
        st.error('423 Locked')
            
def page_6():
    warning()
    st.title('智利问答')
    select = st.selectbox('选择题目', ['1.', '2.'])
    if select == '1.':
        question(1, '作者N不NB?', '不NB', 'a little NB', 'very very NB', 'very very NB', '啊对对对！', 'How dare you are!!!')
    if select == '2.':
        question(2, '我的作品你打几分？', '114514分', '1分', '100分', '1分', '真聪明（还是说你就是这么想的 🤡🤡🤡🤡🤡🤡🤡）！', '有没有一种可能，满分是1分（你这是什么离谱分数！）')

def page_7():
    st.title('先赞后看，是好习惯！！！！！！！')
    for i in range(5):
        a, b, c = st.columns([1, 1, 0.1])
        with a:
            st.title('👍')
        with b:
            st.title('⭐')
        with c:
            st.title('♥️')
    three_push = st.button('一键三连')
    if three_push:
        st.success('205 Reset Content')
        st.balloons()

def question(num, Q, A1, A2, A3, T, T_R, F_R):
    st.subheader('第'+ str(num) + '题:')
    one = st.radio(Q, [A1, A2, A3])
    answer = st.button('提交答案')
    if answer and one == T:
        st.write(T_R)
    elif answer and one != T:
        st.write(F_R)
        st.snow()

def img_change(img, change_c):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            for i in range(3):
                if change_c[i] == 0:
                    c1 = img_array[x, y][i]
                elif change_c[i] == 1:
                    c2 = img_array[x, y][i]
                elif change_c[i] == 2:
                    c3 = img_array[x, y][i]
            img_array[x, y] = (c1, c2, c3)
    return img

def warning():
    st.toast(':red[一定要看看‘入网必看’这一栏！！！]')

if page == '网页介绍':
   page_1()
elif page == '图片处理工具':
    page_2()
elif page == '图片分享与绘制':
    page_3()
elif page == '额外功能——词典':
    page_4()
elif page == '留言区':
    page_5()
elif page == '问答(一定要看看！)':
    page_6()
elif page == '入网必看！！！':
    page_7()  