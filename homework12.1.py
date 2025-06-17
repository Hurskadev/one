import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
      clean_text = []
      inside_tag = False

      for char in html:
          if char == "<":
              inside_tag = True
              continue
          elif char == ">":
              inside_tag = False
              continue
          if not inside_tag:
              clean_text.append(char)

      text = "".join(clean_text)
      lines = text.splitlines()
      cleaned_lines = [line.strip() for line in lines if line.strip()]

      with codecs.open(result_file, "w", "utf-8") as file:
          for line in cleaned_lines:
              file.write(line + "\n")