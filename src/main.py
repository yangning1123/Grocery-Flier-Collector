from rusta import get_rusta_flier_url
from utils import download_pdf_from

# Start script
if __name__ == "__main__":
    rusta_url = get_rusta_flier_url()
    brand_info = [{'brand_name': 'RUSTA', 'url': rusta_url},]

    for brand in brand_info:
        download_pdf_from(**brand)




