import sass
import os

if not os.path.exists('../myapp/static/scss'):
    raise "SCSS dir not exists"

os.chdir('../myapp/static');

sass.compile(dirname=('scss', 'css'), output_style='compressed')
