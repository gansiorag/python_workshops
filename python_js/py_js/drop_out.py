import random
import os
import glob

class dropping_out:
    def __init__(self, name, listing, action):
        self.full_path = os.path.dirname(os.path.abspath(__file__))
        print('self.full_path = ',self.full_path)
        self.zerro_item = 0
        self.listing = listing
        self.type_list = type(listing)
        self.action = action
        self.name_this_wid = name # ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnm')) for d in range(6)])
        self.name_this_file = self.full_path   + '/temp/' + self.name_this_wid +'.fich'
        if not os.path.isfile(self.name_this_file): self.cod_html_write()
        print(self.name_this_file)

    def cod_html_write(self):
        cod_text = ''
        if self.type_list == list:
            print(self.type_list)
            # cod_text += '''<script>'''
            # cod_text += "function f(){var a=document.getElementById('"
            # cod_text += (self.name_this_wid + "').value;"
            #                                   "}"
            #                                   "</script>")
            cod_text += '''<form name="''' + self.name_this_wid + '''" method="post" action="'''
            cod_text += self.action + '''"> Город:<br>'''
            cod_text += '''<select name="''' + self.name_this_wid + '''" id="''' + self.name_this_wid + '''">'''
            for dd in self.listing:
                cod_text += ('''<option value="'''+ dd +'''">''')
                cod_text += (dd +'''</option>''')
        elif self.type_lis == dict:
            print(self.type_list)
        cod_text += ''' </select>
            <input type="submit" value="ok">
            </form>'''


        with open(self.name_this_file, 'w') as r_f:
            r_f.write(cod_text)
        return self.name_this_file

    def cod_html(self):
        return self.name_this_file

    def clear(self):
        file_del = glob.glob(self.full_path   + '/temp/*.fich')
        print(file_del)
        if len(file_del)>0:
            for ff in file_del : os.remove(ff)