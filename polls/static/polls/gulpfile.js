const gulp = require('gulp');
const notify = require('gulp-notify');

gulp.task('wire-bootstrap', function(){
  gulp.src('./vendor/bootstrap-sass/assets/fonts/**/*')
      .pipe(gulp.dest('./fonts'))
      .pipe(notify('Done copying bootstrap fonts to static assets!'));
  gulp.src('./vendor/bootstrap-sass/assets/javascripts/*.js')
      .pipe(gulp.dest('./js/bootstrap'))
      .pipe(notify('Done copying bootstrap scripts to static assets!'));
  gulp.src('./vendor/jquery/dist/*')
      .pipe(gulp.dest('./js/jquery'))
      .pipe(notify('Done copying jquery scripts to static assets!'));
  gulp.src('./vendor/bootstrap-tokenfield/dist/*.js')
      .pipe(gulp.dest('./js'))
      .pipe(notify('Done copying bootstrap-tokenfield scripts to assets!'))
  gulp.src('./vendor/bootstrap-tokenfield/dist/css/*.css')
      .pipe(gulp.dest('./css/bootstrap-tokenfield'))
      .pipe(notify('Done copying bootstrap-tokenfield scripts to assets!'))
});

gulp.task('build',['wire-bootstrap'],function () {

});
