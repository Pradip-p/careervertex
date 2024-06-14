module.exports = {
    content: [
        './job/templates/base.html',
        './job/templates/job/*.html'
        ],
    css: [
        './static/assets/vendor/bootstrap/css/bootstrap.min.css',
        ],
    defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || [],
    // Enable JIT mode
    jit: true,
    whitelist:[
    ]
}

<li class="dropdown"><a href="#"><span>Categories</span> <i class="bi bi-chevron-down dropdown-indicator"></i></a>
          <ul>
              
          </ul>
        </li>