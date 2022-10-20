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
    return Label(part_of, text=text, font=("Arial", font_size, weight), background='#015475')


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
current_result_tab = Frame(notebook, bg='#015475')
settingstab = Frame(notebook, bg='#015475')
notebook.place(x=-1, y=0)

notebook.add(software_download_tab, text="Select software")
notebook.add(current_result_tab, text="Current results")
notebook.add(settingstab, text="Settings")

downloaded_count_label = custom_label_set(current_result_tab, 'No download process has been started yet.', 20)
downloaded_count_label.pack(side=TOP)

instruction_label = custom_label_set(software_download_tab, 'Select the software that\nyou want to download', 20)
instruction_label.pack(side=TOP)
#instruction_label.place(rely=0.03, relx=0.2)

get_architecture = platform.machine()

def insert_elements(given_listbox, search_key):
    if get_architecture == 'AMD64':
        for i, software_name in enumerate(sorted(all_links['for_x64'][search_key].keys())):
            given_listbox.insert(i, software_name)
    elif get_architecture == 'x86':
        for i, software_name in enumerate(sorted(all_links['for_x86'][search_key].keys())):
            given_listbox.insert(i, software_name)


browsers_listbox = Listbox(software_download_tab, height=7, width=16, bg='#015475', font=("Arial", 12), bd=0, selectbackground='blue', selectmode=MULTIPLE, activestyle=NONE, exportselection=False)
insert_elements(browsers_listbox, 'browsers')
browsers_listbox.place(x=0, y=125)

browsers_listbox_scrollbar = Scrollbar(software_download_tab, orient='vertical', command=browsers_listbox.yview)
browsers_listbox['yscrollcommand'] = browsers_listbox_scrollbar.set
browsers_listbox_scrollbar.place(x=149, y=165)

browsers_label = custom_label_set(software_download_tab, 'Browsers', 12, 'bold')
browsers_label.place(x=0, y=100)

utilities_listbox = Listbox(software_download_tab, height=7, width=22, bg='#015475', font=("Arial", 12), bd=0, selectbackground='blue', selectmode=MULTIPLE, activestyle=NONE, exportselection=False)
insert_elements(utilities_listbox, 'utilities')
utilities_listbox.place(x=170, y=125)

utilities_listbox_scrollbar = Scrollbar(software_download_tab, orient='vertical', command=utilities_listbox.yview)
utilities_listbox['yscrollcommand'] = utilities_listbox_scrollbar.set
utilities_listbox_scrollbar.place(x=373, y=165)

utilities_label = custom_label_set(software_download_tab, 'Utilities', 12, 'bold')
utilities_label.place(x=170, y=100)

media_listbox = Listbox(software_download_tab, height=7, width=20, bg='#015475', font=("Arial", 12), bd=0, selectbackground='blue', selectmode=MULTIPLE, activestyle=NONE, exportselection=False)
insert_elements(media_listbox, 'media')
media_listbox.place(x=393, y=125)

media_listbox_scrollbar = Scrollbar(software_download_tab, orient='vertical', command=media_listbox.yview)
media_listbox['yscrollcommand'] = media_listbox_scrollbar.set
media_listbox_scrollbar.place(x=580, y=165)

media_label = custom_label_set(software_download_tab, 'Media', 12, 'bold')
media_label.place(x=390, y=100)

components_listbox = Listbox(software_download_tab, height=7, width=20, bg='#015475', font=("Arial", 12), bd=0, selectbackground='blue', selectmode=MULTIPLE, activestyle=NONE, exportselection=False)
insert_elements(components_listbox, 'components')
components_listbox.place(x=0, y=300)

components_listbox_scrollbar = Scrollbar(software_download_tab, orient='vertical', command=components_listbox.yview)
components_listbox['yscrollcommand'] = components_listbox_scrollbar.set
components_listbox_scrollbar.place(x=185, y=340)

components_label = custom_label_set(software_download_tab, 'Components', 12, 'bold')
components_label.place(x=0, y=275)

out_directory = ""


def change_output_directory():
    global out_directory
    out_directory_before_confirmation = askdirectory(title='Choose the output directory')
    if out_directory_before_confirmation:
        out_directory = out_directory_before_confirmation
        messagebox.showinfo('Output directory saved', 'Output directory saved to \"{}.\"'.format(out_directory))


change_directory_button = Button(software_download_tab, text="Set output directory", font=("Arial", 12), command=change_output_directory)
change_directory_button.place(x=10, y=525)

is_downloading = False


def clear_tab(selected_tab, exception):
    widget_list = selected_tab.winfo_children()
    for w in widget_list:
        if not isinstance(w, exception):
            w.destroy()
            

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
        sum_of_selected = len(browsers_listbox.curselection()) + len(utilities_listbox.curselection()) + len(media_listbox.curselection()) + len(components_listbox.curselection())
        if sum_of_selected == 0:
            return messagebox.showerror('No programs selected', 'No programs were selected.')
        to_divide = 100 / sum_of_selected
        progress = Progressbar(software_download_tab, orient = HORIZONTAL, length = 200, mode = 'determinate')
        percentage_completed = custom_label_set(software_download_tab, text='0% completed.', font_size=12)
        if not progress.winfo_ismapped():
            progress.place(x=0, y=500)
            percentage_completed.place(x=210, y=500)
        else:
            progress['value'] = 0

        is_downloading = True
        downloaded_count = 0
        unable_to_download = []
        clear_tab(current_result_tab, exception=Scrollbar)
        download_result = Label(current_result_tab, text='0/{} downloaded.'.format(sum_of_selected), font=("Arial", 16), bg='#015475')
        download_result.pack(side=TOP, anchor='nw')

        def dict_download(software_dictkey, set_listbox):
            nonlocal downloaded_count
            # software_dictkey: str
            for selected_key in set_listbox.curselection():
                software_name = set_listbox.get(selected_key)
                try:
                    if get_architecture == 'x86':
                        download_from_dict = all_links['for_x86'][software_dictkey]
                    elif get_architecture == 'AMD64':
                        download_from_dict = all_links['for_x64'][software_dictkey]
                    main_download_using_requests(download_from_dict[software_name])
                    downloaded_count += 1
                    download_result.config(text='{}/{} downloaded.'.format(downloaded_count, sum_of_selected))
                except requests.exceptions.ConnectionError:
                    not_downloaded_error_thread = threading.Thread(target=messagebox.showerror, args=["Failed connection establishment", "Failed to download \"{}\". Either the site couldn't be accessed properly, or make sure you are connected to a network.".format(set_listbox.get(selected_key))])
                    not_downloaded_error_thread.start()
                    unable_to_download.append(software_name)
                
                progress['value'] += to_divide
                percentage_completed.config(text='{}% completed.'.format(round(progress['value'])))
                software_download_tab.update_idletasks()

        dict_download('browsers', browsers_listbox)
        dict_download('media', media_listbox)
        dict_download('utilities', utilities_listbox)
        dict_download('components', components_listbox)

        if unable_to_download:
            not_downloaded_list_label = custom_label_set(current_result_tab, "The following couldn't be downloaded:", 16)
            not_downloaded_list_label.pack(side=TOP, anchor='nw')

            for not_downloaded in unable_to_download:
                software_not_downloaded_label = custom_label_set(current_result_tab, not_downloaded, 16)
                software_not_downloaded_label.pack(side=TOP, anchor='nw')


        is_downloading = False
    else:
        messagebox.showwarning('Currently downloading', "There's a current download process happening now.")


def run_download_process_on_thread():
    t = threading.Thread(target=download_selected_software)
    t.start()

download_button = Button(software_download_tab, text="Start download", font=("Arial", 12), command=run_download_process_on_thread)
download_button.place(x=450, y=525)

if __name__ == "__main__":
    root.mainloop()