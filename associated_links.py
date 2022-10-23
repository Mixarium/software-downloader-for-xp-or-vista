import requests

"""
legend:
! - needs updating, because the software is still supported
? - unsure if updating is really needed
"""


def updating_version_of_mypal68():
    try:
        with requests.get('https://api.github.com/repos/Feodor2/Mypal68/releases/latest') as r:
            json_data = r.json()
            return json_data['assets'][0]['browser_download_url']
    except requests.exceptions.ConnectionError:
        return 'https://github.com/Feodor2/Mypal68/releases/download/68.12.5b/mypal-68.12.5.en-US.win32.zip'

 
mypal68_version = updating_version_of_mypal68()


links_dict = {
    'for_x86': {
        'browsers': {
            'Firefox 45.9.0esr': 'https://archive.mozilla.org/pub/firefox/releases/45.9.0esr/win32/en-US/Firefox Setup 45.9.0esr.exe',
            'Firefox 52.9.0esr': 'https://archive.mozilla.org/pub/firefox/releases/52.9.0esr/win32/en-US/Firefox Setup 52.9.0esr.exe',
            'K-Meleon 76.4.6': 'https://o.rthost.win/kmeleon/KM76.4.6-Goanna-20220910.7z', # !
            'Mypal 68': mypal68_version, # !
            'Mypal 29 (Legacy)': 'https://mypal-browser.org/release/mypal-29.3.0.win32.installer.exe',
            'NewMoon': 'https://o.rthost.win/palemoon/palemoon-27.10.0.win32-git-20221015-0be1a20aba-xpmod.7z', # !
            'NewMoon (SSE)': 'https://o.rthost.win/palemoon/palemoon-27.10.0.win32-git-20221015-0be1a20aba-xpmod-sse.7z', # !
            'NewMoon (no SSE)': 'https://o.rthost.win/palemoon/palemoon-27.10.0.win32-git-20221015-0be1a20aba-xpmod-ia32.7z', # !
            'Opera 36': 'http://web.archive.org/web/20191007170021/https://ftp.opera.com/ftp/pub/opera-winxpvista/36.0.2130.80/win/Opera_winxpvista_36.0.2130.80_Setup.exe',
            'Serpent': 'https://o.rthost.win/basilisk/basilisk52-g4.8.win32-git-20221015-3219d2d-uxp-221a4433e-xpmod.7z', # !
            'Serpent (no SSE)': 'https://o.rthost.win/basilisk/basilisk52-g4.8.win32-git-20221015-3219d2d-uxp-221a4433e-xpmod-ia32.7z' # !
        },
        'media': {
            'Adobe Photoshop 7.0': 'http://archive.org/download/photoshop7.0/(AvS) Adobe Photoshop 7.0 FULL (+serial).zip',
            'Audacity': 'http://web.archive.org/web/20220108024104/https://cloud13.send.cm/d/azyrurs36gosj4l4oz2epgxk33pb7f4offexkhzcu4qdhmqy5ntxlftr64f5tu5uhtkaqgvx/audacity-win-2.1.3.exe',
            'Adobe Reader': 'http://web.archive.org/web/20150218042714/http://ardownload.adobe.com/pub/adobe/reader/win/11.x/11.0.08/en_US/AdbeRdr11008_en_US.exe',
            'GIMP': 'http://web.archive.org/web/20180719033756/https://gensho.ftp.acc.umu.se/pub/gimp/gimp/v2.8/windows/gimp-2.8.22-setup.exe',
            'Blender': 'https://download.blender.org/release/Blender2.76/blender-2.76b-windows32.msi',
            'Handbrake (GUI)': 'https://github.com/HandBrake/HandBrake/releases/download/0.9.9/HandBrake-0.9.9-1_i686-Win_GUI.exe',
            'Handbrake (CLI)': 'https://github.com/HandBrake/HandBrake/releases/download/0.9.9/HandBrake-0.9.9-i686-Win_CLI.zip',
            'LibreOffice': 'https://downloadarchive.documentfoundation.org/libreoffice/old/5.4.7.2/win/x86/LibreOffice_5.4.7.2_Win_x86.msi',
            'Lightshot': 'https://app.prntscr.com/build/setup-lightshot.exe',
            'Paint.NET': 'https://web.archive.org/web/20140209153608/http://www.dotpdn.com/files/Paint.NET.3.5.11.Install.zip',
            'ShareX': 'https://github.com/ShareX/ShareX/releases/download/v12.0.0/ShareX-12.0.0-setup.exe',
            'VLC media player': 'https://get.videolan.org/vlc/3.0.17.4/win32/vlc-3.0.17.4-win32.exe' # !
        },
        'utilities': {
            '7-Zip': 'https://www.7-zip.org/a/7z2201.exe', # !
            'Acronis Disk Director 12.5': 'https://dl.acronis.com/s/AcronisDiskDirector12.5_en-US.exe',
            'Autoruns': 'https://web.archive.org/web/20210226223738/https://download.sysinternals.com/files/Autoruns.zip',
            'CDBurnerXP': 'https://web.archive.org/web/20210910131429/https://download.cdburnerxp.se/cdbxp_setup_4.5.8.7128_minimal.exe', # ?
            'Certificate Updater': 'http://i430vx.net/files/misc/Cert_Updater_v1.6.exe',
            'CPU-Z': 'https://download.cpuid.com/cpu-z/cpu-z_2.02-en.exe', # !
            'CrystalDiskInfo': 'https://free.nchc.org.tw/osdn//crystaldiskinfo/77877/CrystalDiskInfo8_17_8.zip', # !
            'CrystalDiskMark': 'https://free.nchc.org.tw/osdn/crystaldiskmark/77539/CrystalDiskMark8_0_4b.zip', # !
            'Dependency Walker': 'https://www.dependencywalker.com/depends22_x86.zip', # ?
            'Everything': 'https://www.voidtools.com/Everything-1.4.1.1022.x86-Setup.exe', # !
            'FFmpeg': 'https://rwijnsma.home.xs4all.nl/files/ffmpeg/ffmpeg-5.2-564-e4ac156-win32-static-xpmod-sse.7z', # !
            'GPU-Z': 'https://archive.org/download/gpu-z.-2.47.0/GPU-Z.2.47.0.exe', # ?
            'HxD': 'https://mh-nexus.de/downloads/HxDSetup.zip',
            'ImgBurn': 'https://download.imgburn.com/SetupImgBurn_2.5.8.0.exe', # !
            'jre8u152 (Java)': 'https://i430vx.net/files/XP/EOL/jre-8u152-windows-i586.exe',
            'nLite': 'http://www.nliteos.com/download/nLite-1.4.9.3.setup.exe',
            'Notepad++': 'https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9.2/npp.7.9.2.Installer.exe',
            'qBittorrent': 'https://archive.org/download/qbittorrent_4.1.9.1_setup/qbittorrent_4.1.9.1_setup.exe',
            'Rufus 2.18': 'https://github.com/pbatard/rufus/releases/download/v2.18/rufus-2.18.exe',
            'Snappy': 'http://sdi-tool.org:8080/releases/SDI_R2201.zip', # !
            'TCP Optimizer': 'https://www.speedguide.net/files/TCPOptimizer.exe',
            'TenFourFoxPEP': 'https://macintoshgarden.org/sites/macintoshgarden.org/files/apps/TenFourFoxPEP_1.zip',
            'Xtreme Download Manager': 'https://archive.org/download/xdmsetup-2018_202209/xdmsetup-2018.msi',
            'youtube-dl': 'https://yt-dl.org/downloads/2021.12.17/youtube-dl.exe', # !
        },
        'components': {
            '.NET Framework AIO': 'https://github.com/abbodi1406/dotNetXP/releases/download/22.06.20/dotNetFx_AIO_x86_20220620.zip', # ?
            'DirectX': 'https://archive.org/download/windows-xp-updates/Windows XP/Microsoft DirectX 9.0C (June 2010) Redistributable/directx_Jun2010_redist.exe',
            'Visual C++ Redist AIO': 'https://github.com/abbodi1406/vcredist/releases/download/v0.35.0/VisualCppRedist_AIO_x86_XP_35.zip', # ?
        },
    },
    'for_x64': {
        'browsers': {
            #'360Chrome v11.0': '{link}', planning to add it sometime
            'Firefox 45.9.0esr': 'https://archive.mozilla.org/pub/firefox/releases/45.9.0esr/win64/en-US/Firefox Setup 45.9.0esr.exe',
            'Firefox 52.9.0esr': 'https://archive.mozilla.org/pub/firefox/releases/52.9.0esr/win64/en-US/Firefox Setup 52.9.0esr.exe',
            'K-Meleon 76': 'https://o.rthost.win/kmeleon/KM76.4.6-Goanna-20220910.7z', # !
            'Mypal 68': mypal68_version, # !
            'Mypal 29 (Legacy)': 'https://mypal-browser.org/release/mypal-29.3.0.win64.installer.exe',
            'NewMoon': 'https://o.rthost.win/palemoon/palemoon-27.10.0.win64-git-20221015-0be1a20aba-xpmod.7z', # !
            'Opera 36': 'http://web.archive.org/web/20191007170021/https://ftp.opera.com/ftp/pub/opera-winxpvista/36.0.2130.80/win/Opera_winxpvista_36.0.2130.80_Setup.exe',
            'Serpent': 'https://o.rthost.win/basilisk/basilisk52-g4.8.win64-git-20221015-3219d2d-uxp-221a4433e-xpmod.7z', # !
        },
        'media': {
            'Adobe Photoshop 7.0': 'http://archive.org/download/photoshop7.0/(AvS) Adobe Photoshop 7.0 FULL (+serial).zip',
            'Adobe Reader': 'http://web.archive.org/web/20150218042714/http://ardownload.adobe.com/pub/adobe/reader/win/11.x/11.0.08/en_US/AdbeRdr11008_en_US.exe',
            'Audacity': 'http://web.archive.org/web/20220108024104/https://cloud13.send.cm/d/azyrurs36gosj4l4oz2epgxk33pb7f4offexkhzcu4qdhmqy5ntxlftr64f5tu5uhtkaqgvx/audacity-win-2.1.3.exe',
            'Blender': 'https://download.blender.org/release/Blender2.76/blender-2.76b-windows64.msi',
            'GIMP': 'http://web.archive.org/web/20180719033756/https://gensho.ftp.acc.umu.se/pub/gimp/gimp/v2.8/windows/gimp-2.8.22-setup.exe',
            'Handbrake (CLI)': 'https://github.com/HandBrake/HandBrake/releases/download/0.9.9/HandBrake-0.9.9-x86_64-Win_CLI.zip',
            'Handbrake (GUI)': 'https://github.com/HandBrake/HandBrake/releases/download/0.9.9/HandBrake-0.9.9-1_x86_64-Win_GUI.exe',
            'LibreOffice': 'https://downloadarchive.documentfoundation.org/libreoffice/old/5.4.7.2/win/x86_64/LibreOffice_5.4.7.2_Win_x64.msi',
            'Lightshot': 'https://app.prntscr.com/build/setup-lightshot.exe',
            'Paint.NET': 'https://web.archive.org/web/20140209153608/http://www.dotpdn.com/files/Paint.NET.3.5.11.Install.zip',
            'ShareX': 'https://github.com/ShareX/ShareX/releases/download/v12.0.0/ShareX-12.0.0-setup.exe',
            'VLC media player': 'https://get.videolan.org/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe', # !
        },
        'utilities': {
            '7-zip': 'https://www.7-zip.org/a/7z2201-x64.exe', # !
            'Acronis Disk Director 12.5': 'https://dl.acronis.com/s/AcronisDiskDirector12.5_en-US.exe',
            'Autoruns': 'https://web.archive.org/web/20210226223738/https://download.sysinternals.com/files/Autoruns.zip',
            'CDBurnerXP': 'https://web.archive.org/web/20210910131429/https://download.cdburnerxp.se/cdbxp_setup_4.5.8.7128_minimal.exe', # ?
            'Certificate Updater': 'http://i430vx.net/files/misc/Cert_Updater_v1.6.exe',
            'CPU-Z': 'https://download.cpuid.com/cpu-z/cpu-z_2.02-en.exe', # !
            'CrystalDiskInfo': 'https://free.nchc.org.tw/osdn//crystaldiskinfo/77877/CrystalDiskInfo8_17_8.zip', # !
            'CrystalDiskMark': 'https://free.nchc.org.tw/osdn/crystaldiskmark/77539/CrystalDiskMark8_0_4b.zip', # !
            'Dependency Walker': 'https://www.dependencywalker.com/depends22_x64.zip', # ?
            'Everything': 'https://www.voidtools.com/Everything-1.4.1.1022.x64-Setup.exe', # !
            'FFmpeg': 'https://rwijnsma.home.xs4all.nl/files/ffmpeg/ffmpeg-5.2-564-e4ac156-win32-static-xpmod-sse.7z', # !
            'GPU-Z': 'https://archive.org/download/gpu-z.-2.47.0/GPU-Z.2.47.0.exe',
            'HxD': 'https://mh-nexus.de/downloads/HxDSetup.zip',
            'ImgBurn': 'https://download.imgburn.com/SetupImgBurn_2.5.8.0.exe', # !
            'jre8u152 (Java)': 'https://archive.org/download/jre-8u152-windows-x64/jre-8u152-windows-x64.exe',
            'nLite': 'http://www.nliteos.com/download/nLite-1.4.9.3.setup.exe',
            'Notepad++': 'https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9.2/npp.7.9.2.Installer.x64.exe',
            'qBittorrent': 'https://archive.org/download/qbittorrent_4.1.9.1_setup/qbittorrent_4.1.9.1_setup.exe',
            'Rufus 2.18': 'https://github.com/pbatard/rufus/releases/download/v2.18/rufus-2.18.exe',
            'Snappy': 'http://sdi-tool.org:8080/releases/SDI_R2201.zip', # !
            'TCP Optimizer': 'https://www.speedguide.net/files/TCPOptimizer.exe',
            'TenFourFoxPEP': 'https://macintoshgarden.org/sites/macintoshgarden.org/files/apps/TenFourFoxPEP_1.zip',
            'Xtreme Download Manager': 'https://archive.org/download/xdmsetup-2018_202209/xdmsetup-2018.msi',
            'youtube-dl': 'https://yt-dl.org/downloads/2021.12.17/youtube-dl.exe', # !
        },
        'components': {
            '.NET Framework AIO': 'https://github.com/abbodi1406/dotNetXP/releases/download/22.06.20/dotNetFx_AIO_x64_20220620.zip', # ?
            'DirectX': 'https://archive.org/download/windows-xp-updates/Windows XP/Microsoft DirectX 9.0C (June 2010) Redistributable/directx_Jun2010_redist.exe',
            'Visual C++ Redist AIO': 'https://github.com/abbodi1406/vcredist/releases/download/v0.35.0/VisualCppRedist_AIO_x64_2k3_35.zip', # ?
        },
    }
}
