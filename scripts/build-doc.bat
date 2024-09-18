SET VERSION=1.7
python setup.py build_sphinx
rem python setup.py build_sphinx -b latex

rem pushd build\sphinx\latex
rem pdflatex pyreadline3.tex
rem pdflatex pyreadline3.tex
rem pdflatex pyreadline3.tex
rem popd

mkdir dist
copy build\sphinx\latex\pyreadline3.pdf dist\pyreadline3-%VERSION%.pdf

xcopy /S /I build\sphinx\html dist\pyreadline3-htmldoc-%VERSION%
