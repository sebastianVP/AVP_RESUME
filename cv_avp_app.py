import streamlit as st
from PIL import Image

#with open("C:/Users/soporte/worspace/AVP_resume/style.css",'r') as f:
with open("style.css",'r') as f:
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
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://github.com/sebastianVP" target="_blank">Alexander Valdez</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#radarspecialist-tools">RadarSpecialist Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

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
-  Graduated.
-  Thesis: `Monitoring System and Early Warning of Alluvium in Huaycoloro's ravine for the Geophysical Institute of Peru and SEDAPAL.` [Thesis](https://repositorio.igp.gob.pe/bitstream/handle/20.500.12816/4449/Valdez%2c%20A.%202015..pdf?sequence=1&isAllowed=y)
-  XXIII CONEIMERA CONGRESS `1st` Place Call for Papers Universidad Nacional de Piura Competition.
''')

#######################
st.markdown('''
## Work Experience
''')

txt('**Radar Specialist**, Instituto Geofisico del Peru' , '2020- Present')

st.markdown('''
- Radar SOPHy: Scaning-system for Observations of Peruvian Hydrometerological-event, Monitoring and maintenance.
[SOPHy](https://doi.org/10.1109/INCAS53599.2021.9666928)
- Project Weather Radar: Equipment design and integration to operate the `1st` Meteorological Radar developed in Peru - SOPHy.
- Project Signal Chain: Develop libraries  for radar data processing.
''')


txt('**Development Engineer**, Instituto Geofisico del Peru','2013-2020')

st.markdown('''
- Project HF Systems: Reading Module development information, process data and plots results. Monitor operation of  transmission and reception stations in different locations within Peru.
- Project TIDDBIT Systems: Monitor status and perform maintenance of transmission stations.
- Project Automatic Beam  Switching: Software test development and hardware with high voltage test and control modules with RF Modules.
- Porject Monitoring Systems and Early Warming of Alluvium: Development of a prototype, design and development of the software acquisition and monitoring, including the development of a Web Interface and field testing.  
- Operation, maintenance and  supervision of the Early Alert System installed in the JRO.
''')

txt('**Jicamarca Engineering Program-Internship**, MIT Haystack Observatory','Jun 2019-Jul 2019')

st.markdown('''
- Project Measuring Meteor winds  using Radio Array of Portable Interferometric Detectors(RAPID).[Link](https://m.facebook.com/MITHaystack/photos/a.1102522826429093/2741805839167442/)
''')

txt('**Research Assistant**, International Science','Jan 2012- Dec 2012')

st.markdown('''
- Development of a Graphical User Interface using Python, QT4Designer, IDE Eric4 and Eclipse.
- Module Development: Reading, processing and visualization using Python. Calculate the Spectra at heights and save data in FITS format.
''')

txt('**Research Assitant**, Universidad Tecnologica del Peru','Oct 2011- Aug 2012')
st.markdown('''
- Development and application of PID and status controllers in laboratories.
- Linux Driver Development.
- Linux for embedded and Real-time Applications.
''')

txt('**Biomedical Research Advisor**, Equipmed Americas','Jan 2011. Dec 2011')
st.markdown('''
- Technical assistance, repair and installation of medical equipment.
''')

######################

st.markdown('''
## RadarSpecialist Tools
''')

txt4('GNURadio','Free & open-source software development toolkit that provides signal processing blocks to implement software radios','https://www.gnuradio.org/')
txt4('SignalChain',' Python-based radar signal processing library developed at the Jicamarca Radio Observatory','http://jro.igp.gob.pe:8082/schain')

#######################

st.markdown('''
## Skills
''')

txt3('Programming','`Python`,`C++`,`Linux`')
txt3('Data processing','`numpy`,`pandas`,`SQL`')
txt3('Data visualization','`matplotlib`,`seaborn`,`plotly`')
txt3('Machine Learning','`scikit-learn`')
txt3('Deep Learning','`TensorFlow`')
txt3('Web development','`Flask`,`HTML`,`CSS`')
txt3('Model deployment','`streamlit`,`Heroku`,`pythonanywhere`')

######################
st.markdown('''
## Social Media
''')

txt2('LinkedIn','https://www.linkedin.com/in/avaldezp/')
txt2('GitHub','https://github.com/sebastianVP')
