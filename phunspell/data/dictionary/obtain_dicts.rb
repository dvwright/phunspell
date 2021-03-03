#!/usr/bin/env ruby

# download dictionaries
# (edit script for when updates needed)
# also see obtain_dicts.sh

require 'net/http'
require 'open-uri'
require 'fileutils'

# af_ZA
# curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/af_ZA/af_ZA.aff > af_ZA.aff
# curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/af_ZA/af_ZA.dic > af_ZA.dic

langs = %w(
af_ZA
an_ES
ar
be_BY
bg_BG
bn_BD
bo
br_FR
bs_BA
cs_CZ
da_DK
el_GR
et_EE
gd_GB
gu_IN
gug
he_IL
hi_IN
hr_HR
hu_HU
is
it_IT
kmr_Latn
ko_KR
lo_LA
lv_LV
ne_NP
nl_NL
oc_FR
pl_PL
pt_BR
pt_PT
ru_RU
si_LK
sk_SK
sl_SI
sq_AL
sw_TZ
te_IN
th_TH
tr_TR
uk_UA
)

def downloadfile(uri, url, lfile)
  # puts "hostname #{uri.hostname} port #{uri.port}"
  Net::HTTP.start(uri.hostname, uri.port, :use_ssl => uri.scheme == 'https') do |http|
    puts "GET #{url}"
    resp = http.get(url)
    puts resp.code
    next unless resp.code > '199' && resp.code < '400'
    puts "#{url} -> #{lfile}"
    open(lfile, 'w') do |file|
      file.write(resp.body)
    end
  end
end

def movefile(lfile, tfile)
  FileUtils.mv(lfile, tfile)
end

def process_std(langs)
  uri = URI('https://raw.githubusercontent.com')
  raw_url = "#{uri}/LibreOffice/dictionaries/master"
  
  langs.each do |e|
    afffile = "#{e}.aff"
    dicfile = "#{e}.dic"
  
    if File.exists? "#{e}/#{afffile}"
      puts "#{e}/#{afffile} exists, skipping download"
      next
    end
  
    # curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/af_ZA/af_ZA.aff > af_ZA.aff
    aff = "#{raw_url}/#{e}/#{afffile}"
    # curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/af_ZA/af_ZA.dic > af_ZA.dic
    dic = "#{raw_url}/#{e}/#{dicfile}"
  
    puts "download #{aff} to #{afffile}"
    downloadfile(uri, aff, afffile)
    puts "move #{afffile} to #{e}"
    movefile(afffile, e)
    puts "sleep 2 seconds"
    sleep 2
    puts "download #{dic} to #{dicfile}"
    downloadfile(uri, dic, dicfile)
    puts "move #{dicfile} to #{e}"
    movefile(dicfile, e)
    puts "sleep 2 seconds"
    sleep 2
  end
end

process_std(langs)
