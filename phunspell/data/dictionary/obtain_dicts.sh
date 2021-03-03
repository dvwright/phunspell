#!/bin/bash

# download dictionaries - non standard locations/scheme

# # special cases
# ca
cd ca && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ca/dictionaries/ca.aff > ca.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ca/dictionaries/ca.dic > ca.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ca/dictionaries/ca-valencia.aff > ca-valencia.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ca/dictionaries/ca-valencia.dic > ca-valencia.dic

# de
cd ../de && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_AT_frami.aff > de_AT_frami.aff \
  && sleep 2 && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_AT_frami.dic > de_AT_frami.dic \
  && sleep 2 && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_CH_frami.aff > de_CH_frami.aff \
  && sleep 2 && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_CH_frami.dic > de_CH_frami.dic \
  && sleep 2 && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_DE_frami.aff > de_DE_frami.aff \
  && sleep 2 && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_DE_frami.dic > de_DE_frami.dic

# en
cd ../en && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_AU.aff > en_AU.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_AU.dic > en_AU.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_CA.aff > en_CA.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_CA.dic > en_CA.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_GB.aff > en_GB.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_GB.dic > en_GB.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_US.aff > en_US.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_US.dic > en_US.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_ZA.aff > en_ZA.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_ZA.dic > en_ZA.dic

# es
cd ../es && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es.aff > es.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es.dic > es.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_AR.aff > es_AR.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_AR.dic > es_AR.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_BO.aff > es_BO.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_BO.dic > es_BO.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CL.aff > es_CL.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CL.dic > es_CL.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CO.aff > es_CO.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CO.dic > es_CO.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CR.aff > es_CR.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CR.dic > es_CR.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CU.aff > es_CU.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CU.dic > es_CU.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_DO.aff > es_DO.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_DO.dic > es_DO.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_EC.aff > es_EC.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_EC.dic > es_EC.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_ES.aff > es_ES.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_ES.dic > es_ES.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_GQ.aff > es_GQ.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_GQ.dic > es_GQ.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_GT.aff > es_GT.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_GT.dic > es_GT.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_HN.aff > es_HN.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_HN.dic > es_HN.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_MX.aff > es_MX.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_MX.dic > es_MX.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_NI.aff > es_NI.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_NI.dic > es_NI.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PA.aff > es_PA.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PA.dic > es_PA.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PE.aff > es_PE.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PE.dic > es_PE.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PH.aff > es_PH.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PH.dic > es_PH.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PR.aff > es_PR.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PR.dic > es_PR.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PY.aff > es_PY.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PY.dic > es_PY.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_SV.aff > es_SV.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_SV.dic > es_SV.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_US.aff > es_US.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_US.dic > es_US.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_UY.aff > es_UY.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_UY.dic > es_UY.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_VE.aff > es_VE.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_VE.dic > es_VE.dic
  
# fr_FR
cd ../fr_FR && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/fr_FR/fr.aff > fr.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/fr_FR/fr.dic > fr.dic

# gl
cd ../gl && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/gl/gl_ES.aff > gl_ES.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/gl/gl_ES.dic > gl_ES.dic
 
# id
cd ../id && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/id/id_ID.aff > id_ID.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/id/id_ID.dic > id_ID.dic
 
# lt_LT
# XXX TODO
cd ../lt_LT && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/lt_LT/lt.aff > lt.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/lt_LT/lt.dic > lt.dic

# no
cd ../no && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/no/nb_NO.aff > nb_NO.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/no/nb_NO.dic > nb_NO.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/no/nn_NO.aff > nn_NO.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/no/nn_NO.aff > nn_NO.aff

# ro
cd ../ro && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ro/ro_RO.aff > ro_RO.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ro/ro_RO.dic > ro_RO.dic

# sr
cd ../sr && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sr/sr-Latn.aff > sr-Latn.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sr/sr-Latn.dic > sr-Latn.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sr/sr.aff > sr.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sr/sr.dic > sr.dic
 
# sv_SE
cd ../sv_SE && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sv_SE/sv_FI.aff > sv_FI.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sv_SE/sv_FI.dic > sv_FI.dic \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sv_SE/sv_SE.aff > sv_SE.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sv_SE/sv_SE.dic > sv_SE.dic

# vi
cd ../vi && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/vi/vi_VN.aff > vi_VN.aff \
  && sleep 2 && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/vi/vi_VN.dic > vi_VN.dic

# zu_ZA
cd ../zu_ZA && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/vi/hyph_zu_ZA.dic > hyph_zu_ZA.dic
