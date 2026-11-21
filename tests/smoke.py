import json,subprocess,time,urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent.parent
import base64
preview_html=(ROOT/'index.html').read_text()
for artfile in (ROOT/'art').glob('*.svg'):
 encoded=base64.b64encode(artfile.read_bytes()).decode()
 preview_html=preview_html.replace('art/'+artfile.name,'data:image/svg+xml;base64,'+encoded)
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
  page=browser.new_page(viewport={'width':1400,'height':1000},device_scale_factor=1)
  page.route('https://fonts.googleapis.com/**',lambda route:route.abort())
  page.route('https://fonts.gstatic.com/**',lambda route:route.abort())
  errors=[]
  page.on('pageerror',lambda e: errors.append(str(e)))
  page.set_content(preview_html,wait_until='domcontentloaded',timeout=12000)
  page.wait_for_timeout(800)
  assert page.locator('.course-card').count()==4,page.locator('.course-card').count()
  assert 'Their syllabi.' in page.locator('h1').inner_text()
  assert '18 SOURCED READING EXCERPTS' in page.locator('#stat-readings').inner_text()
  page.locator('#search').fill('Descartes')
  assert page.locator('.course-card').count()==3
  page.locator('#reset-filters').click()
  assert page.locator('.course-card').count()==4
  page.locator('[data-open="mit-literary-theory"]').click()
  assert page.locator('.dialog .reading').count()==5
  page.locator('[data-add="mit-literary-theory|0"]').click()
  assert page.locator('#counter').inner_text()=='1'
  page.locator('.close').click()
  page.locator('#my-list').click()
  assert 'Oedipus Rex' in page.locator('.drawer').inner_text()
  with page.expect_download() as download_info:page.locator('#export').click()
  download=download_info.value
  assert download.suggested_filename=='my-illicit-syllabus.md'
  # Optional visual regression: page.screenshot(path='desktop-preview.png',full_page=True)
  page.locator('.close').click()
  assert not errors,errors
  phone=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1,is_mobile=True,has_touch=True)
  phone.route('https://fonts.googleapis.com/**',lambda route:route.abort())
  phone.route('https://fonts.gstatic.com/**',lambda route:route.abort())
  phone.set_content(preview_html,wait_until='domcontentloaded',timeout=12000)
  assert phone.locator('.course-card').count()==4
  assert all(r.get('source','').startswith('https://') for c in __import__('json').loads((ROOT/'data/courses.json').read_text()) for r in c['readings'])
  assert phone.evaluate('document.documentElement.scrollWidth<=innerWidth'),phone.evaluate('document.documentElement.scrollWidth')
  # Optional visual regression: phone.screenshot(path='mobile-preview.png',full_page=True)
  browser.close()
 print('PASS: 4 course cards, 18 sourced readings, search, reset, dialog, saving, export, mobile no-overflow, no console errors')
finally:pass
