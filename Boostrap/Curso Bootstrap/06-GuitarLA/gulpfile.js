const { src, dest, watch, series } = require("gulp");

// Compilar CSS
const sass = require("gulp-sass")(require("sass"));
const purgecss = require("gulp-purgecss");
const rename = require("gulp-rename");

// Imagenes
const imagemin = require("gulp-imagemin");

function css(done) {
  src("src/scss/app.scss") // Identificar el archivo principal
    .pipe(sass()) // Compilar SASS
    .pipe(dest("build/css")); // Exportarlo o guardarlo en una ubicación
  done();
}

function cssbuild(done) {
  src("build/css/app.css")
    .pipe(
      rename({
        suffix: ".min",
      })
    )
    .pipe(
      purgecss({
        content: [
          "index.html",
          "base.html",
          "blog.html",
          "entrada1.html",
          "entrada2.html",
          "entrada3.html",
          "entrada4.html",
          "nosotros.html",
          "producto1.html",
          "producto2.html",
          "producto3.html",
          "producto4.html",
          "producto5.html",
          "producto6.html",
          "producto7.html",
          "producto8.html",
          "producto9.html",
          "producto10.html",
          "producto11.html",
          "producto12.html",
          "tienda.html",
        ],
      })
    )
    .pipe(dest("build/css"));

  done();
}

function dev(done) {
  watch("src/scss/**/*.scss", css);
  watch("src/img/**/*");
  done();
}

function imagenes(done) {
  src("src/img/**/*")
    .pipe(imagemin({ optimizationLevel: 3 }))
    .pipe(dest("build/img"));
  done();
}

exports.css = css;
exports.dev = dev;
exports.imagenes = imagenes;
exports.default = series(imagenes, css, dev);
exports.build = series(cssbuild);
