import pyodbc
from datetime import datetime
import hashlib
import time
if __name__ == '__main__':
    t0 = time.time()
    connection = pyodbc.connect('DSN=Implala')
    print(connection)
    connection.chunksize = 5000
    sql = "select addr_key,new_addr_key from adhcisrep.hh_product_detail_bk"
    Cursor = connection.cursor()
    Cursor.execute(sql)
    result = Cursor.fetchall()
    for cRow in result:
      addr_key =  cRow[0]
      new_addr_key = cRow[1]
      hash_object_addr = hashlib.md5(str(addr_key).encode('UTF-8'))
      md5_hash_addr = hash_object_addr.hexdigest()
      print(md5_hash_addr)
      hash_object_new_addr = hashlib.md5(str(new_addr_key).encode('UTF-8'))
      md5_hash_new_addr = hash_object_new_addr.hexdigest()
      print(md5_hash_new_addr)
    Cursor.close()
    connection.close()
