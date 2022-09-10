from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter.ttk import Progressbar
from tkinter import messagebox
import platform
import requests
import threading
import associated_links

all_links = associated_links.links_dict


def custom_label_set(part_of, text: str, font_size, weight='normal'):
    return Label(part_of, text=text, font=("Consolas", font_size, weight), background='#015475')


root = Tk()
root.geometry("600x600")
root.resizable(False, False)
root.title("Software downloader for XP/Vista")

styles = ttk.Style()
styles.theme_use('default')
styles.configure('TNotebook.Tab', background='#015475')
styles.map("TNotebook", background= [("selected", "green3")])
styles.configure("Tab", focuscolor=styles.configure(".")["background"])

notebook = ttk.Notebook(root, height=600, width=600)
software_download_tab = Frame(notebook, bg='#015475')
settingstab = Frame(notebook, bg='#015475')
notebook.place(x=-1, y=0)

notebook.add(software_download_tab, text="Select software")
notebook.add(settingstab, text="Settings")

instruction_label = custom_label_set(software_download_tab, 'Select the software that\nyou want to download', 20)
instruction_label.place(rely=0.03, relx=0.2)

get_architecture = platform.machine()
is_downloading = False

def insert_elements(given_listbox, search_key):
    if get_architecture == 'AMD64':
        for i, software_name in enumerate(all_links['for_x64'][search_key].keys()):
            given_listbox.insert(i, software_name)
    elif get_architecture == 'x86':
        for i, software_name in enumerate(all_links['for_x86'][search_key].keys()):
            given_listbox.insert(i, software_name)


browser_listbox = Listbox(software_download_tab, height=7, width=18, bg='#015475', font=("Consolas", 12), bd=0, selectbackground='blue', selectmode=MULTIPLE, activestyle=NONE, exportselection=False)
insert_elements(browser_listbox, 'browsers')
browser_listbox.place(x=0, y=125)

browser_listbox_scrollbar = Scrollbar(software_download_tab, orient='vertical', command=browser_listbox.yview)
browser_listbox['yscrollcommand'] = browser_listbox_scrollbar.set
browser_listbox_scrollbar.place(x=168, y=165)

browsers_label = custom_label_set(software_download_tab, 'Browsers', 12, 'bold')
browsers_label.place(x=0, y=100)


utilities_listbox = Listbox(software_download_tab, height=7, width=16, bg='#015475', font=("Consolas", 12), bd=0, selectbackground='blue', selectmode=MULTIPLE, activestyle=NONE, exportselection=False)
insert_elements(utilities_listbox, 'utilities')
utilities_listbox.place(x=190, y=125)

utilities_label = custom_label_set(software_download_tab, 'Utilities', 12, 'bold')
utilities_label.place(x=190, y=100)

out_directory = ""


def change_output_directory():
    global out_directory
    out_directory_before_confirmation = askdirectory(title='Choose the output directory')
    if out_directory_before_confirmation:
        out_directory = out_directory_before_confirmation
        messagebox.showinfo('Output directory saved', 'Output directory saved to \"{}.\"'.format(out_directory))


change_directory_button = Button(software_download_tab, text="Set output directory", font=("Consolas", 12), command=change_output_directory)
change_directory_button.place(x=10, y=525)


def main_download_using_requests(url):
    with requests.get(url, stream=True) as r:
        name = url.split('/')[-1]
        name = name.split('dwl=')[-1]
        r.raise_for_status()
        with open(out_directory + "\\" + name, 'wb') as write_file:
            for chunk in r.iter_content(chunk_size=8192):
                write_file.write(chunk)


def download_selected_software():
    global is_downloading
    if not out_directory:
        return messagebox.showerror('Missing output directory', "The output directory hasn't been chosen yet.")
    if not is_downloading:
        sum_of_selected = len(browser_listbox.curselection()) + len(utilities_listbox.curselection())
        if sum_of_selected == 0:
            return messagebox.showerror('No programs selected', 'No programs were selected.')
        to_divide = 100 / (len(browser_listbox.curselection()) + len(utilities_listbox.curselection()))
        progress = Progressbar(software_download_tab, orient = HORIZONTAL, length = 200, mode = 'determinate')
        percentage_completed = custom_label_set(software_download_tab, text='0% completed.', font_size=12)
        if not progress.winfo_ismapped():
            progress.place(x=0, y=500)
            percentage_completed.place(x=210, y=500)
        else:
            progress['value'] = 0

        is_downloading = True
        try:
            for j in browser_listbox.curselection():
                if get_architecture == 'x86':
                    #wget.download(all_links['for_x86']['browsers'][browser_listbox.get(j)], out='E:\c++ shit (plus some python)')
                    main_download_using_requests(all_links['for_x86']['browsers'][browser_listbox.get(j)])
                elif get_architecture == 'AMD64':
                    #wget.download(all_links['for_x64']['browsers'][browser_listbox.get(j)], out='E:\c++ shit (plus some python)')
                    main_download_using_requests(all_links['for_x64']['browsers'][browser_listbox.get(j)])

                progress['value'] += to_divide
                percentage_completed.config(text='{}% completed.'.format(round(progress['value'])))
                software_download_tab.update_idletasks()

            for k in utilities_listbox.curselection():
                if get_architecture == 'x86':
                    #wget.download(all_links['for_x86']['utilities'][utilities_listbox.get(k)], out='E:\c++ shit (plus some python)')
                    main_download_using_requests(all_links['for_x86']['utilities'][utilities_listbox.get(k)])
                elif get_architecture == 'AMD64':
                    # wget.download(all_links['for_x64']['utilities'][utilities_listbox.get(k)], out='E:\c++ shit (plus some python)')
                    main_download_using_requests(all_links['for_x64']['utilities'][utilities_listbox.get(k)])

                progress['value'] += to_divide
                percentage_completed.config(text='{}% completed.'.format(round(progress['value'])))
                software_download_tab.update_idletasks()
        except:
            print('an error has occured (this text will only be displayed temporarily).')
        is_downloading = False
    else:
        messagebox.showwarning('Currently downloading', "There's a current downloading process happening now.")


def run_download_process_on_thread():
    t = threading.Thread(target=download_selected_software)
    t.start()

download_button = Button(software_download_tab, text="Start download", font=("Consolas", 12), command=run_download_process_on_thread)
download_button.place(x=450, y=525)

if __name__ == "__main__":
    root.mainloop()