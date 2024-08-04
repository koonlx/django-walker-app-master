module.exports = {
  content: ['./templates/**/*.html', './static/**/*.js'], // HTML과 JS 파일 경로
  css: ['./static/*.css'], // CSS 파일 경로
  safelist: {
    standard: [/^some-class-to-keep/], // 삭제하지 않을 클래스 목록
  },
};
