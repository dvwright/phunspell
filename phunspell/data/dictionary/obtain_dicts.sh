#!/bin/bash

# download dictionaries - non standard locations/scheme

# # special cases
# ca
cd ca && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ca/dictionaries/ca.aff > ca.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ca/dictionaries/ca.dic > ca.dic

# de
cd ../de && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_AT_frami.aff > de_AT_frami.aff \
  && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_AT_frami.dic > de_AT_frami.dic \
  && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_CH_frami.aff > de_CH_frami.aff \
  && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_CH_frami.dic > de_CH_frami.dic \
  && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_DE_frami.aff > de_DE_frami.aff \
  && \
 curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/de/de_DE_frami.dic > de_DE_frami.dic

# en
cd ../en && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_AU.aff > en_AU.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_AU.dic > en_AU.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_CA.aff > en_CA.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_CA.dic > en_CA.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_GB.aff > en_GB.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_GB.dic > en_GB.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_US.aff > en_US.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_US.dic > en_US.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_ZA.aff > en_ZA.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/en/en_ZA.dic > en_ZA.dic

# es
cd ../es && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es.aff > es.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es.dic > es.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_AR.aff > es_AR.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_AR.dic > es_AR.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_BO.aff > es_BO.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_BO.dic > es_BO.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CL.aff > es_CL.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CL.dic > es_CL.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CO.aff > es_CO.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CO.dic > es_CO.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CR.aff > es_CR.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CR.dic > es_CR.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CU.aff > es_CU.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_CU.dic > es_CU.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_DO.aff > es_DO.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_DO.dic > es_DO.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_EC.aff > es_EC.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_EC.dic > es_EC.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_ES.aff > es_ES.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_ES.dic > es_ES.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_GQ.aff > es_GQ.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_GQ.dic > es_GQ.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_GT.aff > es_GT.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_GT.dic > es_GT.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_HN.aff > es_HN.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_HN.dic > es_HN.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_MX.aff > es_MX.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_MX.dic > es_MX.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_NI.aff > es_NI.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_NI.dic > es_NI.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PA.aff > es_PA.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PA.dic > es_PA.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PE.aff > es_PE.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PE.dic > es_PE.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PH.aff > es_PH.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PH.dic > es_PH.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PR.aff > es_PR.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PR.dic > es_PR.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PY.aff > es_PY.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_PY.dic > es_PY.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_SV.aff > es_SV.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_SV.dic > es_SV.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_US.aff > es_US.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_US.dic > es_US.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_UY.aff > es_UY.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_UY.dic > es_UY.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_VE.aff > es_VE.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/es/es_VE.dic > es_VE.dic
  
# fr_FR
# XXX TODO
cd ../fr_FR && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/fr_FR/

# gl
cd ../gl && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/gl/gl_ES.aff > gl_ES.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/gl/gl_ES.dic > gl_ES.dic
 
# id
cd ../id && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/id/id_ID.aff > id_ID.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/id/id_ID.dic > id_ID.dic
 
# lt_LT
# XXX TODO
cd ../lt_LT && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/lt_LT/

# no
cd ../no && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/no/nb_NO.aff > nb_NO.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/no/nb_NO.dic > nb_NO.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/no/nn_NO.aff > nn_NO.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/no/nn_NO.aff > nn_NO.aff

# ro
cd ../ro && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ro/ro_RO.aff > ro_RO.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ro/ro_RO.dic > ro_RO.dic

# sr
cd ../sr && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sr/sr-Latn.aff > sr-Latn.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sr/sr-Latn.dic > sr-Latn.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sr/sr.aff > sr.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sr/sr.dic > sr.dic
 
# sv_SE
cd ../sv_SE && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sv_SE/sv_FI.aff > sv_FI.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sv_SE/sv_FI.dic > sv_FI.dic \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sv_SE/sv_SE.aff > sv_SE.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sv_SE/sv_SE.dic > sv_SE.dic

# vi
cd ../vi && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/vi/vi_VN.aff > vi_VN.aff \
  && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/vi/vi_VN.dic > vi_VN.dic

# zu_ZA
cd ../zu_ZA && \
  curl https://raw.githubusercontent.com/LibreOffice/dictionaries/master/vi/hyph_zu_ZA.dic > hyph_zu_ZA.dic
