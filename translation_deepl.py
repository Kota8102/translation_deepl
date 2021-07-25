import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

def translate(input_text):

    load_url = "https://www.deepl.com/ja/translator"

    option = Options()                          # オプションを用意
    option.add_argument('--headless')           # ヘッドレスモードの設定を付与
    driver = webdriver.Chrome(options=option) 
    driver.get(load_url)

    input_selector  = "#dl_translator > div.lmt__text > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div.lmt__inner_textarea_container > textarea"
    driver.find_element_by_css_selector(input_selector).send_keys(input_text)

    while True:
        # Output_selector = "#dl_translator > div.lmt__text > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container.lmt__textarea_container_no_shadow > div.lmt__translations_as_text > p.lmt__translations_as_text__item.lmt__translations_as_text__main_translation > button.lmt__translations_as_text__text_btn"
        # Outputtext = driver.find_element_by_css_selector(Output_selector).get_attribute("textContent")
        output_selector = "#target-dummydiv"
        output_text = driver.find_element_by_css_selector(output_selector).get_attribute("textContent")

        if len(output_text) > 3:
            break

        time.sleep(1)
    
    return output_text

def main(input_file="out.txt", output_file="transrated_out.txt"):

    input = input_file 
    output  = open(output_file,"wt") 

    with open(input) as f:
        for line in f:
            temp = line.replace("\n","").strip()
            if len(temp) != 0:
                translated_text = translate(temp)
                print(translated_text)
                output_file.write(translated_text + "\n")
            else:
                output_file.write("\n")
                print(line)

    output_file.close()

if __name__ == "__main__":
    main()
