import streamlit as st

st.set_page_config(
  page_title="SPI_CALC_ECE",
  page_icon='🔣'
 
)
#data
dt={"A+":10,"A":9,"B+":8,"B":7,"C+":6,"C":5,"IF":0,"FF":0}
#heading
st.title("SPI CALCULATOR FOR ECE Vth SEM")
st.text("Nirma university")
st.title("  ")
st.title("  ")
col1,col2=st.columns([1,1])
col3,col4=st.columns([1,1])
col5,col6=st.columns([1,1])

with col1:
  vlsi=st.selectbox("VLSI",["A+","A","B+","B","C+","C","IF","FF"])
with col2:
  dsp=st.selectbox("DSP",["A+","A","B+","B","C+","C","IF","FF"])
with col3:
  dcomm=st.selectbox("DCOMM",["A+","A","B+","B","C+","C","IF","FF"])
with col4:
  sl=st.selectbox("SL/IP",["A+","A","B+","B","C+","C","IF","FF"])  
with col5:
  cl=st.selectbox("CLOUD(OPEN ELECTIVE)",["A+","A","B+","B","C+","C","IF","FF"])
with col6:
  pd=st.selectbox("PD(HUMANITY POOL)",["A+","A","B+","B","C+","C","IF","FF"])  
but=st.button("calculate")  
if but==True:
  li= {"VLSI": vlsi, "DSP": dsp, "DCOMM": dcomm, "SL/IP": sl, "Cloud": cl, "PD": pd}
  tc=22
  tg=0
  for key,val in li.items():
    if key in ["Cloud", "PD"]: 
       tg=tg+(3*dt[val])    
    else:
      tg=tg+(4*dt[val])
  re=tg/tc 
  res=round(re,2)
  per=(res-0.5)*10
  PER=round(per,2)
  col6,col7=st.columns([1,1]) 
  with col6:  
      st.subheader("Your SPI:")
      st.success(f"{res}") 
  with col7:  
      st.subheader("Your Percentage(%):")
      st.success(f"{PER}")           