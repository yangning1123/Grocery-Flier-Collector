from rusta import get_rusta_flier_url
from ica import get_ica_flier_url
from utils import download_pdf_from

# Start script
if __name__ == "__main__":
    rusta_url = get_rusta_flier_url()
    ica_url = get_ica_flier_url()
    brand_info = [{'brand_name': 'RUSTA', 'url': rusta_url},
                  {'brand_name': 'HEMKOP', 'url': 'https://hemkop.eo.se/hkp/4138.pdf'},
                  {'brand_name': 'ICA', 'url': ica_url}]

    for brand in brand_info:
        download_pdf_from(**brand)




