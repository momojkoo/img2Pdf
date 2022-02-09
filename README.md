# Img2Pdf
- 사진들을 모아서 pdf로 변환 (makePdf)
- pdf 파일 합치기 (pdfMerge)
- pdf 각 페이지를 이미지로 저장하기 (myPdf2jpg)

## 사전설정
1. requirements.txt 를 사용하여 pip 설치
2. .py 및 .batch 파일들을 복사해둔다
3. 각 batch 파일에서 PROGRAMPATH 경로 확인 및 수정

## 사용법
### makePdf
	1. makePdf.bat 파일을 이미지가 있는 폴더로 복사한다.
	2. makePdf.bat 파일을 실행한다.
	3. 현재 폴더에 있는 이미지 파일(jpg, gif, png) 파일이 정렬되어 하나의 pdf(output.pdf)로 생성된다.

### pdfMerge
	1. makePdf.bat 파일을 pdf 파일들이 있는 폴더로 복사한다.
	2. makePdf.bat 파일을 실행한다.
	3. pdf 파일들이 하나로 합쳐져 하나의 pdf(merged.pdf)로 생성된다.

### myPdf2jpg
	1. makeJpgs.bat 파일을 pdf 파일이 있는 폴더로 복사한다.
	2. makeJpgs.bat 파일을 실행한다.
	3. pdf 파일과 같은 이름의 폴더에 jpg 파일들이 생성된다.
