def on_page_markdown(markdown, page,  **kwargs):
	text = "\n Thank you"
	print(page.url, page.canonical_url)
	#return "\n".join([markdown, page.canonical_url])


def on_page_content(html, page,  **kwargs):
	text = "\n Thank you"
	# print(page.url, page.canonical_url)

def on_post_page(output, page,  **kwargs):
	text = "\n Thank you"
	# print(page.url, page.canonical_url)
	if page.url == "blog/2023-07-17-how-to-generate-a-python-package-in-5m/":
		print(page.content)