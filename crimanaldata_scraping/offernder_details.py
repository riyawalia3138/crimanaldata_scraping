from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = Options()

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
  
driver.get('https://www.icrimewatch.net/results.php?SubmitAllSearch=1&AgencyID=54567')
agree_btn = driver.find_element(By.ID,"agree").click()
continue_btn = driver.find_element(By.ID,"continue").click()
time.sleep(2)
urls = driver.find_elements(By.TAG_NAME,'a')
url_data =[]
for u in urls:
    hrURL = u.get_attribute('href')
    if hrURL:
        if hrURL not in url_data and "https://www.icrimewatch.net/offenderdetails.php?OfndrID=" in hrURL:
            url_data.append(hrURL)
driver.close()
###############################################################################
all_data=[]
tableData = []
c1=0
for link in url_data:
    try:
        count = 0
        driver1 = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver1.get(link)
        agree_btn = driver1.find_element(By.ID,"agree").click()
        continue_btn = driver1.find_element(By.ID,"continue").click()
        html=driver1.page_source
        soup = BeautifulSoup(html, 'html.parser')
        pimage=driver1.find_elements(By.XPATH,"//div[contains(@class, 'webviewOnly')]/img")
        print("images",pimage[1].get_attribute('src'))
        details =  soup.findAll('table')
        with open ('page2.txt','w') as file:
            file.write(str(details))
        for tab in details:
            data = tab.findAll('table')
            if count == 2 and len(data) > 0:
                tableData = data
                with open ('page.txt','w') as file:
                    file.write(str(data))
                    #values = BeautifulSoup(str(data),'html.parser')
            if len(data) > 0:
                count = count + 1
        
        tdata = []
        tDataText = []
        ofndr_details={}
        print('length',len(tableData))
        tData0 = tableData[0].findAll("td")
        for x in tData0:
            tdata.append(x.text)
        tData1 = tableData[1].findAll("td")
        
        for x in tData1:
            tdata.append(x.text)
        res = []
        for sub in tdata:
            res.append(sub.replace(u'\xa0', '').replace(u'\n', ''))
        print(res)
        num_len =res.index('Name:')
        reg_len =res.index('Registration #:')
        try:
            alias_len =res.index('Aliases:')
            print('alias_len',alias_len)
        except Exception as e:
            alias_len = 0
            print("alias error",e)
        ver_len =res.index('Last Verification Date:')
        phy_len =res.index('Physical Description')
        age_len =res.index('• Age:')
        hgt_len =res.index('• Height:')
        sex_len =res.index('• Sex:')
        wgt_len =res.index('• Weight:')
        race_len =res.index('• Race:')
        eye_len =res.index('• Eyes:')
        hair_len =res.index('• Hair:')
        scr_len =res.index('• Scars/Tattoos:')
        addr_len = res.index('Address')
        otr_add_len = res.index('Other Known Addresses')
        desc_lens=[i for i, v in enumerate(res) if v == '• Description:' ]
        print(len(desc_lens),desc_lens)
        #desc_len = desc_lens[0]#res.index('• Description:')
        dt_convit_lens= [i for i, v in enumerate(res) if v == '• Date Convicted:' ]#res.index('• Date Convicted:')
        convit_st_lens= [i for i, v in enumerate(res) if v == '• Conviction State:' ]#res.index('• Conviction State:')
        rls_dt_lens= [i for i, v in enumerate(res) if v == '•Release Date:' ]#res.index('•Release Date:')
        details_lens= [i for i, v in enumerate(res) if v == '• Details:' ]#res.index('• Details:')
        if len(desc_lens) == 1:
            desc_len=desc_lens[0]
            dt_convit_len = dt_convit_lens[0]
            convit_st_len = convit_st_lens[0]
            rls_dt_len = rls_dt_lens[0]
            details_len = details_lens[0]
        elif len(desc_lens) == 2: 
            #desc_lenss=[i for i, v in enumerate(res) if v == '• Description:' ]
            desc_len=desc_lens[0]
            desc_len1=desc_lens[1]
            print("len",desc_len,desc_len1)
            dt_convit_len = dt_convit_lens[0]
            dt_convit_len1 = dt_convit_lens[1]
            convit_st_len = convit_st_lens[0]
            convit_st_len1 = convit_st_lens[1]
            rls_dt_len = rls_dt_lens[0]
            rls_dt_len1 = rls_dt_lens[1]
            details_len = details_lens[0]
            details_len1 = details_lens[1]
        elif len(desc_lens) == 3: 
            desc_len=desc_lens[0]
            desc_len1=desc_len=desc_lens[1]
            desc_len2=desc_lens[2]
            dt_convit_len = dt_convit_lens[0]
            dt_convit_len1 = dt_convit_lens[1]
            dt_convit_len2 = dt_convit_lens[2]
            convit_st_len = convit_st_lens[0]
            convit_st_len1 = convit_st_lens[1]
            convit_st_len2 = convit_st_lens[2]
            rls_dt_len = rls_dt_lens[0]
            rls_dt_len1 = rls_dt_lens[1]
            rls_dt_len2 = rls_dt_lens[2]
            details_len = details_lens[0]
            details_len1 = details_lens[1]
            details_len2 = details_lens[2]
        elif len(desc_lens) == 4: 
            desc_len=desc_lens[0]
            desc_len1=desc_len=desc_lens[1]
            desc_len2=desc_lens[2]
            desc_len3=desc_len=desc_lens[3]
            print("values are here",desc_lens,"values",desc_lens[0],"--",desc_len,desc_len1,desc_len2,desc_len3)
            dt_convit_len = dt_convit_lens[0]
            dt_convit_len1 = dt_convit_lens[1]
            dt_convit_len2 = dt_convit_lens[2]
            dt_convit_len3 = dt_convit_lens[3]
            convit_st_len = convit_st_lens[0]
            convit_st_len1 = convit_st_lens[1]
            convit_st_len2 = convit_st_lens[2]
            convit_st_len3 = convit_st_lens[3]
            rls_dt_len = rls_dt_lens[0]
            rls_dt_len1 = rls_dt_lens[1]
            rls_dt_len2 = rls_dt_lens[2]
            rls_dt_len3 = rls_dt_lens[3]
            details_len = details_lens[0]
            details_len1 = details_lens[1]
            details_len2 = details_lens[2]
            details_len3 = details_lens[3]
        elif len(desc_lens) == 0:
            pass 
        cmt_len = res.index('Comments')
        info_len= res.index('Share this information with a friend! ')
        name= str(res[num_len:reg_len]).split(",")[1].translate( { ord("]"): None } )
        if alias_len == 0:
            reg = str(res[reg_len:ver_len]).split(",")[1].translate( { ord("]"): None } )
            alias = ''
        else:
            reg = str(res[reg_len:alias_len]).split(",")[1].translate( { ord("]"): None } )
            aliass = str(res[alias_len:ver_len]).split(",")[1:]#.split(",")[1].translate( { ord("]"): None } )
            alias=str(aliass).translate( { ord("]"): None } ).translate( { ord("["): None } )
        verfication_dt= str(res[ver_len:phy_len]).split(",")[1].translate( { ord("]"): None } )
        offender_img = pimage[1].get_attribute('src')
        age= str(res[age_len:hgt_len]).split(",")[1].translate( { ord("]"): None } )
        height= str(res[hgt_len:sex_len]).split(",")[1].translate( { ord("]"): None } )
        sex= str(res[sex_len:wgt_len]).split(",")[1].translate( { ord("]"): None } )
        weight= str(res[wgt_len:race_len]).split(",")[1].translate( { ord("]"): None } )
        race= str(res[race_len:eye_len]).split(",")[1].translate( { ord("]"): None } )
        eyes= str(res[eye_len:hair_len]).split(",")[1].translate( { ord("]"): None } )
        hair= str(res[hair_len:scr_len]).split(",")[1].translate( { ord("]"): None } )
        scars= str(str(res[scr_len:addr_len]).split(",")[1:]).translate( { ord("]"): None } ).translate( { ord("["): None } )
        add= str(res[addr_len:otr_add_len]).split(",")[1:-1]
        addr=str(add).translate( { ord("]"): None } ).translate( { ord("["): None } )
        comments= str(res[cmt_len:info_len]).split(",")[1].translate( { ord("]"): None } )
        desc_count =0
        desc_data=[]
        
                
        if len(desc_lens) == 0:
            desc= ''
            dt_convict=''
            convict_st =''
            release_dt=''
            dtls=''
        else:
            for m in range(len(desc_lens)):
                print("m",m , desc_lens[m],"desc_count",desc_count,"desc length",desc_lens[m])
                desc= str(res[desc_lens[m]:dt_convit_lens[m]]).split(",")[1].translate( { ord("]"): None } )
                dt_convict= str(res[dt_convit_lens[m]:convit_st_lens[m]]).split(",")[1].translate( { ord("]"): None } )
                convict_st= str(res[convit_st_lens[m]:rls_dt_lens[m]]).split(",")[1].translate( { ord("]"): None } )
                release_dt= str(res[rls_dt_lens[m]:details_lens[m]]).split(",")[1].translate( { ord("]"): None } )
                if desc_count == len(desc_lens)-1:
                    dtls= str(str(res[details_lens[m]:cmt_len]).split(",")[1:]).translate( { ord("]"): None } ).translate( { ord("["): None } )
                    
                    print("now met condition")
                else:
                    dtls= str(str(res[details_lens[m]:desc_lens[m+1]]).split(",")[1:]).translate( { ord("]"): None } ).translate( { ord("["): None } )
                    print("not met yet",dtls)
                desc_count = desc_count+1
                desc_dict ={}
                desc_dict['description']= desc
                desc_dict['date_convited']= dt_convict
                desc_dict['convited_state']= convict_st
                desc_dict['release_date']= dt_convict
                desc_dict['details']= release_dt

                print("desc",desc,"dt_convict",dt_convict,"convict_st",convict_st,"release_dt",release_dt,"dtls",dtls)
                desc_data.append(desc_dict)
                #dtls=str(dtlss).translate( { ord("]"): None } )
        print("desc_data",desc_data)
       

        ofndr_details['name'] = name
        ofndr_details['registartion'] = reg
        ofndr_details['alias'] = alias
        ofndr_details['verification_date'] = verfication_dt
        ofndr_details['offender_img'] = offender_img
        ofndr_details['age'] = age
        ofndr_details['height'] = height
        ofndr_details['sex'] = sex
        ofndr_details['weight'] = weight
        ofndr_details['race'] = race
        ofndr_details['eyes'] = eyes
        ofndr_details['hair'] = hair
        ofndr_details['scars'] = scars
        ofndr_details['address'] = addr
        ofndr_details['description'] = desc
        ofndr_details['date_convited'] = dt_convict
        ofndr_details['convited_state'] = convict_st
        ofndr_details['release_date'] = release_dt
        ofndr_details['comments'] = comments
        ofndr_details['details'] = dtls
        
        all_data.append(ofndr_details)
        c1 =c1+1
        if c1 ==3: 
            print("all_data",all_data)
            import csv
            csv_columns = ['name','registartion', 'alias','verification_date','offender_img','age','height','sex','weight','race','eyes','hair','scars','address','description','date_convited','convited_state','release_date','comments','details']
            csv_file = "details.csv"
            try:
                with open(csv_file, 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for data in all_data:
                        writer.writerow(data)
            except IOError:
                print("I/O error")
            break
    except Exception as e:
        print("error",e)
        pass
    

