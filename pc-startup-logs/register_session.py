from datetime import datetime
log_file = open('logs.txt', 'r')
logs = log_file.read()
log_file.close()
current_session = datetime.now()
current_session_log = current_session.strftime('Date: %d/%m/%Y Time: %H:%M:%S\n')
logs += current_session_log
log_file = open('logs.txt', 'w')
log_file.write(logs)
log_file.close()