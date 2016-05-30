const gulp = require('gulp');
const livereload = require('gulp-livereload');
const exec = require('gulp-exec');
const notify = require('gulp-notify');

gulp.task('collectstatic', function() {
    let options = {
      continueOnError: false, // default = false, true means don't emit error event
      pipeStdout: false, // default = false, true means stdout is written to file.contents
      customTemplatingThing: "test" // content passed to gutil.template()
    };
    let reportOptions = {
    	err: true, // default = true, false means don't write err
    	stderr: true, // default = true, false means don't write stderr
    	stdout: true // default = true, false means don't write stdout
    }
    gulp.src('./**/**')
      .pipe(exec('python manage.py collectstatic', options))
      .pipe(exec.reporter(reportOptions))
      .pipe(notify("Done collecting static assets!"));
});


gulp.task('watch',['collectstatic'], function () {
    livereload.listen();
    gulp.watch('polls/static/polls/css/*/*.scss', ['collectstatic']).on('change', livereload.changed);
    gulp.watch('polls/static/polls/js/**/*.js').on('change', livereload.changed);
    gulp.watch('polls/templates/**/*.html').on('change', livereload.changed);
});
