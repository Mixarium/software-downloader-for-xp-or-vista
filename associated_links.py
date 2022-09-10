import requests

def updating_version_of_mypal68():
    with requests.get('https://api.github.com/repos/Feodor2/Mypal68/releases/latest') as r:
        json_data = r.json()
        return json_data['assets'][0]['browser_download_url']

 
mypal68_version = updating_version_of_mypal68()


links_dict = {
    'for_x86': {
        'browsers': {
            'Firefox 45.9.0esr': 'https://archive.mozilla.org/pub/firefox/releases/45.9.0esr/win32/en-US/Firefox Setup 45.9.0esr.exe',
            'Firefox 52.9.0esr': 'https://archive.mozilla.org/pub/firefox/releases/52.9.0esr/win32/en-US/Firefox Setup 52.9.0esr.exe',
            'Mypal 68': mypal68_version,
            'Mypal 29 (Legacy)': 'https://mypal-browser.org/release/mypal-29.3.0.win32.installer.exe',
            'Serpent': 'https://o.rthost.win/basilisk/basilisk52-g4.8.win32-git-20220903-3219d2d-uxp-64173440f-xpmod.7z',
        },
        'media': {
            'VLC media player': 'https://get.videolan.org/vlc/3.0.17.4/win32/vlc-3.0.17.4-win32.exe'
        },
        'utilities': {
            '7-Zip': 'https://www.7-zip.org/a/7z2201.exe',
            'Autoruns': 'http://live.sysinternals.com/autoruns.exe',
            'CDBurnerXP': 'https://web.archive.org/web/20210910131429/https://download.cdburnerxp.se/cdbxp_setup_4.5.8.7128_minimal.exe',
            'Everything': 'https://www.voidtools.com/Everything-1.4.1.1020.x86-Setup.exe',
            'FFmpeg': 'https://rwijnsma.home.xs4all.nl/files/ffmpeg/ffmpeg-5.2-564-e4ac156-win32-static-xpmod-sse.7z',
            'HxD': 'https://mh-nexus.de/downloads/HxDSetup.zip',
            'ImgBurn': 'https://download.imgburn.com/SetupImgBurn_2.5.8.0.exe',
            'jre8u152 (Java)': 'https://i430vx.net/files/XP/EOL/jre-8u152-windows-i586.exe',
            'Rufus 2.18': 'https://github.com/pbatard/rufus/releases/download/v2.18/rufus-2.18.exe',
            'Snappy': 'http://sdi-tool.org:8080/releases/SDI_R2201.zip',
        }
    },
    'for_x64': {
        'browsers': {
            'Firefox 45.9.0esr': 'https://archive.mozilla.org/pub/firefox/releases/45.9.0esr/win64/en-US/Firefox Setup 45.9.0esr.exe',
            'Firefox 52.9.0esr': 'https://archive.mozilla.org/pub/firefox/releases/52.9.0esr/win64/en-US/Firefox Setup 52.9.0esr.exe',
            'Mypal 68': mypal68_version,
            'Mypal 29 (Legacy)': 'https://mypal-browser.org/release/mypal-29.3.0.win64.installer.exe',
            'Serpent': 'https://o.rthost.win/basilisk/basilisk52-g4.8.win64-git-20220903-3219d2d-uxp-64173440f-xpmod.7z',
        },
        'media': {
            'VLC media player': 'https://get.videolan.org/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
        },
        'utilities': {
            '7-zip': 'https://www.7-zip.org/a/7z2201-x64.exe',
            'Autoruns': 'http://live.sysinternals.com/autoruns.exe',
            'CDBurnerXP': 'https://web.archive.org/web/20210910131429/https://download.cdburnerxp.se/cdbxp_setup_4.5.8.7128_minimal.exe',
            'Everything': 'https://www.voidtools.com/Everything-1.4.1.1020.x64-Setup.exe',
            'FFmpeg': 'https://rwijnsma.home.xs4all.nl/files/ffmpeg/ffmpeg-5.2-564-e4ac156-win32-static-xpmod-sse.7z',
            'HxD': 'https://mh-nexus.de/downloads/HxDSetup.zip',
            'ImgBurn': 'https://download.imgburn.com/SetupImgBurn_2.5.8.0.exe',
            'jre8u152 (Java)': 'https://archive.org/download/jre-8u152-windows-x64/jre-8u152-windows-x64.exe',
            'Rufus 2.18': 'https://github.com/pbatard/rufus/releases/download/v2.18/rufus-2.18.exe',
            'Snappy': 'http://sdi-tool.org:8080/releases/SDI_R2201.zip',
        }
    }
}
