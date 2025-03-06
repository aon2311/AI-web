import streamlit as st


def display_home():
    st.title ("ปัญญาประดิษฐ์ (Artificial Intelligence)")


    # AI (Artificial Intelligence) คืออะไร?
    st.markdown(" ##  (Artificial Intelligence) คืออะไร?")
    st.image("https://engineering.fb.com/wp-content/uploads/2016/12/grid-AI.jpg", caption="รูปภาพจาก https://engineering.fb.com/2016/12/01/ml-applications/artificial-intelligence-revealed/")
    st.markdown('<div class="text_indent">AI หรือ Artificial Intelligence (ปัญญาประดิษฐ์) เป็นเทคโนโลยีที่มีความสามารถในการแก้ปัญหาเหมือนมนุษย์ การทำงานของ AI สามารถจดจำภาพ เขียนบทกวี และคาดการณ์ตามข้อมูลได้ </div>', unsafe_allow_html=True)
    st.markdown('<br><div class="normal-text">ยกตัวอย่างง่าย ๆ ที่เราใช้งาน AI กันทุกวัน: <br> •ระบบแนะนำภาพยนตร์บน Netflix'
                        '<br>•ผู้ช่วยเสียงอัจฉริยะอย่าง Siri และ Google Assistant'
                        '<br> •ระบบค้นหาสินค้าบนแพลตฟอ</div>', unsafe_allow_html=True)

    # เบื้องหลังความฉลาดของ AI

    st.markdown(" ### เบื้องหลังความฉลาดของ AI ")
    st.image("https://static.independent.co.uk/2023/08/11/16/2048x1536.png?quality=75&width=1250&crop=3%3A2%2Csmart&auto=webp", caption="รูปภาพจาก https://www.independent.co.uk/tech/ai-artificial-intelligence-threat-debate-b2391587.html")
    st.markdown("เบื้องหลัง AI เป็นกระบวนการที่เรียกว่า Machine Learning (ML) และ Deep Learning (DL) ซึ่งเปรียบเสมือนการฝึกสมองของคอมพิวเตอร์ให้รู้จักแยกแยะข้อมูล")
    st.markdown("#### Machine Learning (ML):")
    st.markdown("     การทำให้ระบบคอมพิวเตอร์สามารถเรียนรู้ได้ด้วยตนเองโดยใช้ข้อมูล” Machine Learning เป็น subset ของ AI")
    st.markdown("ตัวอย่าง: การทำนายราคาหุ้น หรือการกรองสแปมในอีเมล") 
    st.markdown(" ")
    st.markdown("#### Deep Learning (DL)")
    st.markdown("     หนึ่งในเทคโนโลยี Machine Learning ที่สร้างขึ้นมาเพื่อใช้สอนปัญญาประดิษฐ์ (AI) โดย Deep Learning จะใช้โครงข่ายประสาทเทียม (Artificial Neural Network: ANN) ในการเรียนรู้ ทำให้มีความแม่นยำในการประมวลผลข้อมูลที่มีความซับซ้อนและชุดข้อมูลขนาดใหญ่") 
    st.markdown("ตัวอย่าง: การประมวลผลภาพและวิดีโอ ")
    st.markdown(" ")
    st.markdown(" ### AI เลียนแบบมนุษย์ได้ยังไง")
    st.markdown("     AI เลียนแบบมนุษย์ได้โดยการเรียนรู้จากข้อมูลที่เก็บมา ซึ่งประกอบด้วยรูปแบบพฤติกรรมและการตัดสินใจของมนุษย์ ผ่านเทคนิคต่างๆ ")
    st.markdown("แต่ในกรณีที่มี data น้อย การฝึก AI อาจจะยากขึ้น เพราะ AI จะไม่สามารถเรียนรู้หรือสร้างโมเดลที่แม่นยำได้จากข้อมูลที่จำกัด ยิ่งได้ข้อมูลดี AIก็จะยิ่งทำงานได้ดียิ่งขึ้น") 

    st.markdown(" ### Machine Learning: เมื่อ AI เรียนรู้จากข้อมูลจริงเพื่อแก้ปัญหาในโลกจริง")
    st.markdown("AI จะฉลาดได้ต้องมีข้อมูลที่หลากหลายและมากพอให้เรียนรู้ จากนั้น AI จะค่อย ๆ พัฒนาความสามารถผ่านการสร้างโมเดลที่เหมาะสมในการแก้ปัญหา เช่น การแยกแยะภาพ การทำนายข้อมูล หรือการตัดสินใจที่ซับซ้อนในโปรเจกต์นี้ เราจะประยุกต์ใช้ เทคนิคการเรียนรู้ของ Machine Learning ที่หลากหลายและสำคัญ เช่น")
    st.markdown("     • Decision Tree: เทคนิคที่สร้างการตัดสินใจเป็นลำดับขั้นตอน โดยใช้โครงสร้างแบบต้นไม้")                
    st.markdown("     • K-Nearest Neighbors (KNN): วิธีการที่ค้นหาข้อมูลที่คล้ายกันมากที่สุดรอบตัว เพื่อคาดการณ์ผลลัพธ์")             
    st.markdown("     • Support Vector Regression (SVR): เทคนิคที่ช่วยในการทำนายข้อมูลต่อเนื่อง")               
    st.markdown("     • Ensemble Method (Stacking): การรวมโมเดลหลายตัวเข้าด้วยกันเพื่อเพิ่มประสิทธิภาพในการทำนาย")             
    st.markdown("     • Neural Networks: โครงข่ายประสาทเทียมที่สามารถเรียนรู้ข้อมูลเชิงลึกได้เหมือนสมองมนุษย์")                     
            
    st.markdown("### การประเมินผลและเป้าหมายของโปรเจกต์")
    st.markdown("     ผลลัพธ์จากโมเดลเหล่านี้จะถูกวิเคราะห์และประเมินด้วย ตัวชี้วัดทางสถิติ เพื่อค้นหาโมเดลที่มีประสิทธิภาพดีที่สุด โดยเป้าหมายหลักคือการนำโมเดลมาแก้ปัญหาในสถานการณ์จริง พร้อมเปรียบเทียบประสิทธิภาพระหว่างแต่ละโมเดล เพื่อหาแนวทางการประยุกต์ใช้ที่เหมาะสมที่สุด")

    st.markdown(" ### โมเดลการเรียนรู้")
    st.markdown("#### 1. Decision Tree")
    st.image("https://www.mastersindatascience.org/wp-content/uploads/sites/54/2022/05/tree-graphic.jpg",caption="รูปภาพจาก https://www.mastersindatascience.org/learning/machine-learning-algorithms/decision-tree/")
    st.markdown("โมเดลที่ไม่เป็นเชิงเส้น (Non-linear) ที่ทำการแบ่งข้อมูลเป็นกลุ่มย่อยๆ ตามค่าของคุณลักษณะต่างๆ เพื่อให้สามารถตัดสินใจได้ โมเดลนี้สามารถอธิบายการตัดสินใจได้ง่ายและเหมาะสำหรับการทำความเข้าใจวิธีการที่โมเดลตัดสินใจจากข้อมูลที่ป้อนเข้าไป")
    st.markdown(" ")
    st.markdown("#### 2. K-Nearest Neighbors (KNN)")
    st.image("https://www.nerd-data.com/content/images/size/w1000/2023/10/image-14.png",caption="รูปภาพจาก https://www.nerd-data.com/knn/")
    st.markdown("โมเดลที่ง่ายแต่มีประสิทธิภาพ โดยการจัดประเภทข้อมูลใหม่ๆ ขึ้นอยู่กับความใกล้เคียงของข้อมูลนั้นกับข้อมูลในชุดฝึกฝน โมเดลนี้เชื่อมโยงสมมติฐานที่ว่า สิ่งที่คล้ายกันมักจะอยู่ใกล้เคียงกัน")
    st.markdown(" ")
    st.markdown("#### 3. Support Vector Regression (SVR)")
    st.image("https://i0.wp.com/spotintelligence.com/wp-content/uploads/2024/05/support-vector-regression-svr.jpg?resize=1024%2C576&ssl=1",caption="รูปภาพจาก https://spotintelligence.com/2024/05/08/support-vector-regression-svr/")
    st.markdown("เทคนิคการถดถอย (Regression) ที่มุ่งหาค่าที่ดีที่สุดในขณะที่อนุญาตให้มีขอบเขตของข้อผิดพลาด โดย SVR เหมาะสมกับข้อมูลในมิติสูงและเมื่อมีความสัมพันธ์ที่ไม่เป็นเชิงเส้นระหว่างข้อมูล")
    st.markdown(" ")
    st.markdown("#### 4. Ensemble Method (Stacking)")
    st.image("https://miro.medium.com/v2/resize:fit:1100/format:webp/1*DM1DhgvG3UCEZTF-Ev5Q-A.png",caption="รูปภาพจาก https://medium.com/@brijesh_soni/stacking-to-improve-model-performance-a-comprehensive-guide-on-ensemble-learning-in-python-9ed53c93ce28")
    st.markdown("คือเทคนิคที่ใช้การรวมหลายๆ โมเดลเข้าด้วยกันเพื่อให้ผลลัพธ์ที่แม่นยำยิ่งขึ้น โดยจะนำผลลัพธ์จากโมเดลต่างๆ มารวมกันแล้วใช้โมเดลใหม่ในการทำนายผลสุดท้าย กระบวนการนี้ช่วยลดความผิดพลาดของโมเดลเดียว และสามารถทำให้ผลลัพธ์มีความแม่นยำมากขึ้น")
    st.markdown(" ")
    st.markdown("#### 5. Neural Networks")
    st.image("https://www.qtravel.ai/wp-content/uploads/2023/07/sieci-neuronowe-grafika-1024x759.png",caption="รูปภาพจาก https://www.qtravel.ai/blog/what-are-neural-networks-and-what-are-their-applications/")
    st.markdown("โมเดลที่ได้รับแรงบันดาลใจจากสมองมนุษย์ ใช้สำหรับการจดจำลวดลายและการทำนายผล Neural Networks เป็นโมเดลที่มีความยืดหยุ่นสูงและสามารถจับความสัมพันธ์ที่ซับซ้อนได้จากข้อมูล")
    st.markdown(" ")


    st.markdown(" ### การนำมาประยุกต์ใช้ในการทำโปรเจกต์")
    st.markdown(" ##### การทำนายคุณภาพอากาศ")
    st.markdown("การทำนายคุณภาพอากาศ ไม่เพียงแค่ช่วยให้เราทราบข้อมูลที่แม่นยำ แต่ยังช่วยให้เราสามารถตัดสินใจได้ดีกว่าในการดูแลสุขภาพและป้องกันมลพิษทางอากาศได้อย่างมีประสิทธิภาพ.")
    st.markdown("โดยโปรเจคนี้เราจะทำการพัฒนาระบบทำนายคุณภาพอากาศ โดยใช้ข้อมูลสำคัญๆ เช่น")
    st.markdown("• Particulate Matter 2.5 (PM2.5)")
    st.markdown("• อุณหภูมิ (Temperature)")
    st.markdown("• Ozone(O3)")
    st.markdown("• Carbon Dioxide(CO2)")
    st.markdown("• ความชื้น (Humidity)")




