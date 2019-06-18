import pyb,time
statements=[]
message=''
def LOAD(wifi):
    global message
    global statements
    while True:
        if wifi.any()>0:
            data=wifi.read()
            if data==b'OOFF':
                try:
                    log=open('/sd/main.py','w')
                except OSError:
                    log=open('/flash/main.py','w')	
                print(statements)
                for statement in statements:
                    pyb.LED(2).on()
                    log.write(statement)
                    time.sleep_ms(100)
                    pyb.LED(2).off()
                    time.sleep_ms(100)
                log.close()
            else:
                statements.append(data)
        elif len(message)>0:#free time ,send the message to  wifi
            pyb.LED(3).on()
            wifi.write(message)
            time.sleep_ms(200)
            pyb.LED(3).off()
            message=''
            time.sleep_ms(200)
