import uuid
import hashlib
import impala_execute as hd
import pyodbc
from impala.dbapi import connect
from googletrans import Translator
import pythainlp.util as pyUtil
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import jaydebeapi


def get_hive_jdbc_con(HIVE_HOST, HIVE_PORT, HIVE_USERNAME, HIVE_PASSWORD):
    driver = "org.apache.hive.jdbc.HiveDriver"
    conn_url = "jdbc:hive2://{host}:{port}/default".format(host=HIVE_HOST, port=HIVE_PORT)
    auth_lst = [HIVE_USERNAME, HIVE_PASSWORD]
    conn = jaydebeapi.connect(driver, conn_url, auth_lst)
    print(conn)
    return conn


def generate_uuid():
    # Use a breakpoint in the code line below to debug your script.
    print(uuid.uuid1())  # Press Ctrl+F8 to toggle the breakpoint.
    print(uuid.uuid4())  # Press Ctrl+F8 to toggle the breakpoint.
    arrroad = [
        'กรุงเกษม', 'กรุงเทพกรีฑา', 'กรุงเทพ-นนทบุรี', 'กรุงธนบุรี', 'กรุงแมน', 'กล้วยน้ำไทตัดใหม่', 'กลันตัน', 'กะออม',
        'กระออม', 'กัลปพฤกษ์', 'กัลยาณไมตรี', 'กาญจนาภิเษก', 'กำนันแม้น', 'กำแพงเพชร', 'กำแพงเพชร 1', 'กำแพงเพชร 2',
        'กำแพงเพชร 3', 'กำแพงเพชร 4', 'กำแพงเพชร 5', 'กำแพงเพชร 6', 'กำแพงเพชร 7', 'กิ่งแก้ว', 'กิจพานิช', 'เกษมราษฎร์',
        'แก้ว', 'แก้วเงินทอง', 'โกสุมรวมใจ', 'ไกรสีห์',
        'ขวัญ', 'ขาว', 'ข้าวสาร', 'ข้าวหลาม', 'ขุมทอง-ลำต้อยติ่ง', 'เขียวไข่กา',
        'ครุใน', 'คลองเก้า', 'คลองถมวัดพิเรนทร์', 'คลองถมวัดสระเกศ', 'คลองถมวัดโสมนัส', 'คลองลำเจียก', 'คลองลำปัก',
        'คลองสิบ-คลองสิบสี่', 'คอนแวนต์', 'คุ้มเกล้า', 'คู้บอน', 'คู้-คลองสิบ', 'เคหะร่มเกล้า',
        'งามวงศ์วาน', 'จตุโชติ', 'จรัญสนิทวงศ์', 'จรัสเมือง', 'จรัสเวียง', 'จรูญเวียง', 'จอมทอง', 'จอมทองบูรณะ',
        'จักรพงษ์', 'จักรพรรดิพงษ์', 'จักรเพชร', 'จักรวรรดิ', 'จันทน์', 'จันทน์เก่า', 'จันทรุเบกษา', 'จารุเมือง',
        'จึงเจริญพาณิชย์', 'เจริญกรุง', 'เจริญนคร', 'เจริญพัฒนา', 'เจริญเมือง', 'เจริญรัถ', 'เจริญราษฎร์', 'เจริญเวียง',
        'เจ้าคำรพ', 'เจ้าคำรบ', 'เจ้าคุณทหาร', 'เจ้าพระยาสยาม', 'เจ้าฟ้า', 'แจ้งวัฒนะ',
        'ฉลองกรุง', 'ฉิมพลี', 'เฉลิมเขต 1', 'เฉลิมเขต 2', 'เฉลิมเขต 3', 'เฉลิมเขต 4', 'เฉลิมพงษ์',
        'เฉลิมพระเกียรติ ร.9', 'แฉล้มนิมิตร',
        'ชักพระ', 'ชัยพฤกษ์', 'ช่างอากาศอุทิศ', 'ชิดลม', 'เชตุพน', 'เชิดวุฒากาศ', 'เชียงใหม่', 'เชื้อเพลิง',
        'เชื่อมคลองมอญ', 'เชื่อมสัมพันธ์', 'โชคชัย 4',
        'ณ ระนอง',
        'ดวงพิทักษ์', 'ดาวข่าง', 'ดำรงรักษ์', 'ดินแดง', 'ดินแดง 1', 'ดินสอ', 'ดิสมาร์ค', 'เดชะตุงคะ', 'เดโช',
        'ตรีเพชร', 'ตรีมิตร', 'ตะนาว', 'ตานี', 'ตีทอง', 'เตชะวณิช',
        'ทรงวาด', 'ทรงสวัสดิ์', 'ทรงเสริม', 'ทรัพย์', 'ทรัพย์สิน', 'ทวีวัฒนา', 'ทวีวัฒนา-กาญจนาภิเษก', 'ทหาร',
        'ทหารอากาศอุทิศ', 'ทับยาว', 'ท่าเกษม', 'ท่าข้าม', 'ทางรถไฟสายเก่าปากน้ำ', 'ท่าดินแดง', 'ท้ายวัง', 'ทุ่งมังกร',
        'เทศบาลนฤมาณ', 'เทศบาลนิมิตใต้', 'เทศบาลนิมิตเหนือ', 'เทศบาลรังรักษ์ใต้', 'เทศบาลรังรักษ์เหนือ',
        'เทศบาลรังสรรใต้', 'เทศบาลรังสรรเหนือ', 'เทศบาลรังสฤษดิ์ใต้', 'เทศบาลรังสฤษดิ์เหนือ', 'เทศบาลสงเคราะห์',
        'เทอดดำริ', 'เทอดไท', 'เทิดราชัน', 'เทียมร่วมมิตร', 'ไทยรามัญ',
        'ธนิยะ',
        'นครไชยศรี', 'นครปฐม', 'นครราชสีมา', 'นครลุง', 'นครสวรรค์', 'นนทรี', 'นราธิวาสราชนครินทร์', 'นเรศ', 'นวมินทร์',
        'นวลจันทร์', 'นักกีฬาแหลมทอง', 'นาคนิวาส', 'นาคราช', 'นางลิ้นจี่', 'นาวงประชาพัฒนา', 'นิคมมักกะสัน',
        'นิมิตใหม่', 'นิลเหมนิยม', 'นี้จงสวัสดิ์',
        'บรมราชชนนี', 'บรรทัดทอง', 'บริพัตร', 'บวรนิเวศน์', 'บางกระดี่', 'บางขุนเทียน', 'บางขุนเทียน-ชายทะเล',
        'บางขุนนนท์', 'บางแค', 'บางเชือกหนัง', 'บางนา-ตราด', 'บางบอน 1', 'บางบอน 2', 'บางบอน 3', 'บางบอน 4', 'บางบอน 5',
        'บางบอนสายเดิม', 'บางไผ่', 'บางพรม', 'บางระมาด', 'บางแวก', 'บ้านหม้อ', 'บำรุงเมือง', 'บึงขวาง', 'บุญศิริ',
        'บุรีภิรมย์', 'บูรณศาสตร์', 'บูรพา', 'แบนชะโด', 'แบรสต์',
        'ประชาชื่น', 'ประชาทร', 'ประชาธิปก', 'ประชาธิปไตย', 'ประชาพัฒนา', 'ประชาร่วมใจ', 'ประชาราษฎร์ สาย 1',
        'ประชาราษฎร์ สาย 2', 'ประชาราษฎร์บำเพ็ญ', 'ประชาสงเคราะห์', 'ประชาสำราญ', 'ประชาสุข', 'ประชาอุทิศ',
        'ประดิพัทธิ์', 'ประดิษฐ์มนูธรรม', 'ประมวญ', 'ประเสริฐมนูกิจ', 'ปรินายก', 'ปั้น', 'ปากน้ำกระโจมทอง',
        'ปากน้ำฝั่งเหนือ', 'แปลงนาม',
        'ผดุงด้าว', 'ผดุงพันธ์',
        'พญาไท', 'พญาไม้', 'พรหมราษฎร์', 'พระจันทร์', 'พระพิทักษ์', 'พระพิพิธ', 'พระยาสุเรนทร์', 'พระราม 1', 'พระราม 2',
        'พระราม 3', 'พระราม 4', 'พระราม 5', 'พระราม 6', 'พระราม 9', 'พระสุเมรุ', 'พระอาทิตย์', 'พรานนก', 'พลับพลาไชย',
        'พ่วงศิริ', 'พหลโยธิน', 'พะเนียง', 'พัฒน์พงศ์', 'พัฒนา', 'พัฒนาการ', 'พัฒนาชนบท', 'พัฒนาชนบท 2', 'พัฒนาชนบท 3',
        'พัฒนาชนบท 4', 'พาณิชยการธนบุรี', 'พาดสาย', 'พาหุรัด', 'พิชัย', 'พิบูลสงคราม', 'พิษณุโลก', 'พีรพงษ์',
        'พุทธบูชา', 'พุทธมณฑล สาย 1', 'พุทธมณฑล สาย 2', 'พุทธมณฑล สาย 3', 'เพชรเกษม', 'เพชรบุรี', 'เพชรพระราม',
        'เพชรอุทัย', 'เพลินจิต', 'เพาะพานิชย์', 'เพิ่มสิน', 'แพร่งนรา', 'แพร่งภูธร', 'แพร่งสรรพศาสตร์', 'โพธิ์แก้ว',
        'เฟื่องนคร',
        'ภาณุรังษี', 'ภุชงค์', 'โภคี',
        'มหรรณพ', 'มหาจักร', 'มหาไชย', 'มหานคร', 'มหาพฤฒาราม', 'มหาราช', 'มหาเศรษฐ์', 'มเหสักข์', 'มไหสวรรย์',
        'มอเตอร์เวย์', 'มังกร', 'มาเจริญ', 'มิตรพันธ์', 'มิตรภาพไทย-จีน', 'มิตรไมตรี', 'มิตรไมตรี 1', 'มิตรไมตรี 2',
        'มิตรไมตรี 3', 'มีนพัฒนา', 'แมนไท', 'ไมตรีจิต',
        'ยมราชสุขุม', 'ยังพัธนา', 'ยานนาวา', 'ยี่สิบสองกรกฎาคม 1', 'ยี่สิบสองกรกฎาคม 2', 'ยี่สิบสองกรกฎาคม 3',
        'ยี่สิบสองกรกฎาคม 4', 'ยี่สิบสองกรกฎาคม 5', 'ยุคล 1', 'ยุคล 2', 'เย็นจิต', 'เย็นอากาศ', 'เยาวพานิชย์',
        'เยาวราช', 'แยกสวนสยาม', 'โยธา', 'โยธา 1', 'โยธินพัฒนา', 'โยธี',
        'ร่มเกล้า', 'ร่วมจิตต์', 'ร่วมพัฒนา', 'รองเมือง', 'ระนอง 1', 'ระนอง 2', 'รัชดาภิเษก', 'รัชดา-รามอินทรา',
        'รัชมงคลประสาธน์', 'รางน้ำ', 'ราชดำเนินกลาง', 'ราชดำเนินนอก', 'ราชดำเนินใน', 'ราชดำริ', 'ราชบพิธ', 'ราชปรารภ',
        'ราชพฤกษ์', 'ราชมนตรี', 'ราชวงศ์', 'ราชวิถี', 'ราชินี', 'รามคำแหง', 'รามคำแหง 2', 'รามบุตรี', 'รามอินทรา',
        'ราษฎร์นิมิตร', 'ราษฎร์บูรณะ', 'ราษฎร์พัฒนา', 'ราษฎร์ร่วมใจ', 'ราษฎร์รัฐพัฒนา', 'ราษฎร์อุทิศ',
        'ริมคลองประปาฝั่งขวา', 'ริมคลองประปาฝั่งซ้าย', 'รุ่งประชา',
        'ลงท่า', 'ลาซาล', 'ลาซาล-แบริ่ง', 'ลาดกระบัง', 'ลาดปลาเค้า', 'ลาดพร้าว', 'ลาดพร้าววังหิน', 'ลาดหญ้า', 'ลำไทร',
        'ลำพูนไชย', 'ลำมะเขือขื่น', 'ลิขิต', 'ลูกหลวง', 'เลียบคลองเนินทราย', 'เลียบคลองบางพรม', 'เลียบคลองปทุม',
        'เลียบคลองผดุงกรุงเกษม', 'เลียบคลองพิทยาลงกรณ์', 'เลียบคลองภาษีเจริญฝั่งใต้', 'เลียบคลองภาษีเจริญฝั่งเหนือ',
        'เลียบคลองมอญ', 'เลียบคลองลำกอไผ่', 'เลียบคลองสอง', 'เลียบคลองสิบสามฝั่งตะวันตก', 'เลียบคลองสิบสามฝั่งตะวันออก',
        'เลียบทะเลสาบ', 'เลียบวารี',
        'วงศ์สว่าง', 'วรจักร', 'วังเจ้าสาย', 'วังเดิม', 'วังหลัง', 'วัชรพล', 'วัฒนธรรม', 'วัดเวฬุวนาราม', 'วัดสุขใจ',
        'วัดใหม่เจริญราษฎร์', 'วิทยุ', 'วิบูลย์สาธุกิจ', 'วิบูลย์สาธุกิจ', 'วิวัฒน์เวียง', 'วิสุทธิกษัตริย์', 'วุฒากาศ',
        'ศรีธรรมาธิราช', 'ศรีนครินทร์', 'ศรีบูรพา', 'ศรีวรา', 'ศรีเวียง', 'ศรีอยุธยา', 'ศาลาแดง', 'ศาลาธรรมสพน์',
        'ศิริเกษม', 'ศิริพงษ์', 'ศุภมิตร', 'เศรษฐศิริ', 'เศรษฐศิริ 2', 'สกุลดี',
        'สตรีวิทยา 2', 'สนามไชย', 'สมเด็จเจ้าพระยา', 'สมเด็จพระเจ้าตากสิน', 'สมเด็จพระปิ่นเกล้า', 'สรงประภา', 'สรณคมน์',
        'สรรพาวุธ', 'สราญรมย์', 'สวนผัก', 'สวนพลู', 'สวนสยาม', 'สวนอ้อยซอยกลาง', 'สวรรคโลก', 'สวัสดิการ 1',
        'สวัสดิการ 2', 'สวัสดิการ 3', 'สว่าง', 'สะแกงาม', 'สะพานพุทธ', 'สังคมสงเคราะห์', 'สังคโลก', 'สังฆประชา',
        'สังฆสันติสุข', 'สันติภาพ', 'สาทรใต้', 'สาทรเหนือ', 'สาธุประดิษฐ์', 'สามวา', 'สามเสน', 'สายไหม', 'สารสิน',
        'สารีบุตร', 'สารีบุตร-ทับยาว', 'สาลีรัฐวิภาค', 'สิบสามห้าง', 'สิรินธร', 'สี่พระยา', 'สีลม', 'สีหบุรานุกิจ',
        'สุขสวัสดิ์', 'สุขาภิบาล 2', 'สุขาภิบาล 5', 'สุขาภิบาลบางระมาด', 'สุขุมวิท', 'สุโขทัย', 'สุคนธสวัสดิ์',
        'สุคันธาราม', 'สุดประเสริฐ', 'สุทธาวาส', 'สุทธิสารวินิจฉัย', 'สุนทรโกษา', 'สุพรรณ', 'สุรวงศ์', 'สุรศักดิ์',
        'สุวินทวงศ์', 'สุเหร่าคลองหนึ่ง', 'เสนานิคม 1', 'เสรีไทย', 'เสือป่า', 'แสนเกษม', 'แสมดำ',
        'หทัยมิตร', 'หทัยราษฎร์', 'หนองแขม-วัดศรีนวล', 'หนองระแหง', 'หน้าพระธาตุ', 'หน้าพระลาน', 'หน้าหับเผย',
        'หม่อมเจ้าสง่างาม สุประดิษฐ์', 'หมู่บ้านเศรษฐกิจ', 'หลวง', 'หลวงพรตพิทยพยัต', 'หลวงแพ่ง', 'หลักเมือง',
        'หลังสวน', 'หลานหลวง', 'หอวัง', 'หัวหมาก',
        'อนันตนาค', 'อนามัยงามเจริญ', 'อนุวงศ์', 'อยู่เย็น', 'อยู่วิทยา', 'อรุณอมรินทร์', 'อโศก-ดินแดง', 'อโศกมนตรี',
        'อ่อนนุช', 'อังรีดูนังต์', 'อัศวพิเชษฐ์', 'อัษฎางค์', 'อัสสัมชัญ', 'อาจณรงค์', 'อำนวยสงคราม', 'อินทรพิทักษ์',
        'อินทราวาส', 'อิสรภาพ', 'อุณากรรณ', 'อุดมสุข', 'อุทยาน', 'อู่ทองนอก', 'อู่ทองใน', 'เอกชัย',
        '60 พรรษามหาราชินี'
    ];
    i=0;
    for iAraay in arrroad:
        i = i +1 ;
        hash_object = hashlib.md5(iAraay.encode('UTF-8'))
        md5_hash = hash_object.hexdigest()
        print(str(i) + ")."+ iAraay + "=" + md5_hash)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hd.execute_query("select 1 as id")
    """
    translator = Translator()
    print(str('MUEANG Roi Et District ').title())
    tranthai = translator.translate(str('Khiri Mat District').title(), dest='th')
    print(tranthai.text)
    isThai = pyUtil.isthai("ดสหดก")
    print(isThai)
    DEFAULT_DB = 'default'
    DEFAULT_SERVER = '10.37.40.1'
    DEFAULT_PORT = 10000
    DEFAULT_DOMAIN = 'PAM01-PRD01.IBM.COM'
    
    database = "default"
    server = "hdppr2-hive.true.care"
    port = "10000"
    domain = "truecorp"

    url = "jdbc:hive2://{host}:{port}/{database};principal=hive/{host}@{domain}".format(
        host=server, port=port, database=database, domain=domain
    )
    user ='Pornc25'
    pwd= 'ri=yp;b=b9l6;iiI'
    cx=get_hive_jdbc_con(server,port,user,pwd)
    print(cx)
    conn = connect(url)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM adhcisrep.tee_master_thai_4_key")
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

    #generate_uuid()
    hash_object = hashlib.md5(str("30381นคมอตสหกรรมสนสครบรษทฟจอซจกดจษฎวถคกขมมองสมทรสครสมทรสคร74000").encode('UTF-8'))
    md5_hash = hash_object.hexdigest()
    print(md5_hash)
    hash_object = hashlib.md5(str("55612รนดนมMILRBARนฝยมองชยภมชยภม36000").encode('UTF-8'))
    md5_hash = hash_object.hexdigest()
    print(md5_hash)
    hash_object = hashlib.md5(str("544สรจตรศรสชนลยสขทย64130").encode('UTF-8'))
    md5_hash = hash_object.hexdigest()
    print(md5_hash)
    hash_object = hashlib.md5(str("9028ปงปหวยดนชยพร54110").encode('UTF-8'))
    md5_hash = hash_object.hexdigest()
    print(md5_hash)
    """
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
