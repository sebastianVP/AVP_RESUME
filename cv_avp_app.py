import streamlit as st
from PIL import Image

with open("C:/Users/soporte/worspace/AVP_resume/style.css",'r') as f:
   st.markdown('<style>{}</style>'.format(f.read()),unsafe_allow_html=True)

#########################

st.write('''
#  Alexander Valdez, Electron. Eng.
##### *Resume*
''')


image = Image.open('FOTO_AVP.jpeg')
st.image(image,width=150)


st.markdown('## Summary',unsafe_allow_html=True)
st.info('''
- Highly accomplished radar design and software development electronic engineer.
- Track record of success in developing libraries for signal processing and designing acquisition radars systems.
- Research engineer with extensive knowledge in engineering principles, leadership and application 
research apply within government institutions.
- Project leader with the ability to build productive cross-functional teamas.
''')


#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Science in Computer Science** (Student), *Univ. Nacional de Ingenieria*, Lima-Peru','2022-2024')
st.markdown('''
- Focus    : Design, implementation and modification of software with the aim of guaranteeing that it is of high quality.
- Knowledge: Data Structure, algorithms, image processing, natural language processing and Machine Learning..
- Studying : The behavior and interactions of natural and artificial systems that store, process, access, and communicate information.
''')

txt('**Bachelors of Science** (Electronic Engineer), *Univ. Nacional de Ingenieria* , Lima-Peru','2006-2010')
st.markdown('''
-  Graduated
-  Thesis: `Monitoring System and Early Warning of Alluvium in Huaycoloro's ravine for the Geophysical Institute of Peru and SEDAPAL` [ Link ](https://repositorio.igp.gob.pe/bitstream/handle/20.500.12816/4449/Valdez%2c%20A.%202015..pdf?sequence=1&isAllowed=y)
-  XXIII CONEIMERA CONGRESS `1st` Place Call for Papers Universidad Nacional de Piura Competition.
''')

#######################
st.markdown('''
## Work Experience
''')

txt('**Radar Specialist**, Instituto Geofisico del Peru' , '2020- Present')

st.markdown('''
- Project Weather Radar: Equipment design and integration to operate the `1st` Meteorological Radar developed in Peru
- Project Signal Chain: Develop libraries  for radar data processing.
-
''')







