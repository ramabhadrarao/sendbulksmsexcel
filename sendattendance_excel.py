import streamlit as st
import pandas as pd
import requests
from PIL import Image
#st.title("Swarnandhra Whatsapp Message Sender")

##########################################################
# .streamlit/secrets.toml
def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True




#########################################################











st.set_page_config(page_title="Swarnandhra", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

if check_password():
        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        image = Image.open('logo1.png')

        st.image(image, caption='SWARNANDHRA Whatsapp Messages Sending Application')
        uploaded_file = st.file_uploader("Choose a CSV file",type=['xls','xlsx'])
        
        if uploaded_file:
            all_sheet = pd.ExcelFile(uploaded_file)   
            sheets = all_sheet.sheet_names
            st.write(str(sheets))
            for i in range(len(sheets)):
                data=pd.read_excel(uploaded_file,sheet_name = sheets[i])
                st.header("Branch Name::"+str(sheets[i])+"::::Total Students:"+str(data.shape[0]))
                st.dataframe(data)
                if not data.empty:     
                    for index,x in data.iterrows():
			            if int(x[7]) == 0:
                        	str1="http://bulkwhatsapp.live/wapp/api/send?apikey=e28a534874e64cc2949b8dba67bac699&mobile="
	
        	                str2=str(x[6])
                	        str3="&msg=""\"Dear Parent,  %0a Your son or daughter :"
                        	str5=str(x[0]+"("+x[1]+")")
                        	#if int(x[7]) == 0:
                        	#str6=", Present to college and Attended:: "
                        	#else:
                            str6=", Absent to The College ,:: "   
                        	#str7=str(x[7])+":: Classes."
                        	str8="  %0a This for Your Information.Regards & Thanks  %0a Principal , %0a  SWARNANDHRA COLLEGE OF ENGINEERING AND TECHNOLOGY.  %0a Thank you\""
                        	result=str1+str2+str3+str5+str6+str8
                        	#st.write(str3+str5+str6+str7+str8)
                        	res = requests.get(result)
                        	response=res.json()
                        	#st.write(response["status"])
                        	if(response["status"] == "success"): 
                                	st.success("Sms Sent Successfully"+str2+"-"+str5+"-"+str7)
                        	else:
                                	st.warning("Sms Not Sent "+str2+"-"+str5+"-"+str7)
                        	#st.balloons()
st.write("Developed by Rama Bhadra Rao Maddu & Dr Bomma Rama Krishna")

