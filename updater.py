import requests
import zipfile
import os

#"https://github.com/wowsims/cata/releases/download/v0.0.26/wowsimcata-windows.exe.zip"
r = requests.get("https://github.com/wowsims/cata/releases/")
cwd = os.getcwd()


def get_version(req_obj):
	html_dump = list()
	version = None
	for i in r.iter_lines():
		if i:
			if "latest" in str(i):
				break

			html_dump.append(str(i))

	for i in html_dump:
		if "/wowsims/cata/releases/tag/" in i:
			first = i.split("/wowsims/cata/releases/tag/", 1)[1]
			version = first.split('"')[0]

	return version

def write_version_to_file(version):
	file = cwd + "\\version.txt"

	with open(file, "w") as f:
		f.write(version)

def get_version_from_file():
	file = cwd + "\\version.txt"
	try:
		with open(file, "r") as f:
			return f.readlines()[0]
	except Exception as e:
		print("version file not found, assuming first use or other issue...")
		return ""

def write_and_extract_sim(req_obj):

	file = cwd + '\\test.zip'

	with open(file, 'wb') as f:
		f.write(req_obj.content)

	with zipfile.ZipFile(file, 'r') as zip_ref:
		zip_ref.extractall(cwd)

	os.remove(file)


def main():
	version = get_version(r)
	if version != get_version_from_file():
		latest_path = "https://github.com/wowsims/cata/releases/download/{}/wowsimcata-windows.exe.zip".format(version)
		r_latest = requests.get(latest_path)
		write_and_extract_sim(r_latest)
		write_version_to_file(version)
	else:
		print("Current version: {} is latest on github".format(version))

main()