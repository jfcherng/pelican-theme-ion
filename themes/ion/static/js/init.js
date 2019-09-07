SITEURL = SITEURL == null ? '.' : SITEURL;

/**
 * responsive
 *
 * We comment out all "href" attributes because we want to load them via
 * <link rel="stylesheet" href="..." media="screen and (max-width:...px)" />
 * to avoid the starting brief flicker.
 *
 * @see https://github.com/ajlkn/skel/issues/110
 */
skel.init({
    reset: false,
    breakpoints: {
        // Global.
        global: {
            range: '*',
            // href: SITEURL + '/theme/css/style.css',
            containers: 1440,
            grid: {
                gutters: {
                    vertical: '15px',
                    // vertical: '4em',
                    horizontal: 0
                }
            }
        },
        // XLarge.
        xlarge: {
            range: '-1600',
            // href: SITEURL + '/theme/css/style-xlarge.css',
            containers: 1200
        },
        // Large.
        large: {
            range: '-1200',
            // href: SITEURL + '/theme/css/style-large.css',
            containers: 960,
            grid: {
                gutters: {
                    // vertical: '2.5em'
                }
            },
            viewport: {
                scalable: false
            }
        },
        // Medium.
        medium: {
            range: '-992',
            // href: SITEURL + '/theme/css/style-medium.css',
            containers: '95%',
            grid: {
                collapse: 1
            }
        },
        // Small.
        small: {
            range: '-768',
            // href: SITEURL + '/theme/css/style-small.css',
            containers: '95%',
            grid: {
                gutters: {
                    // vertical: '1.25em'
                }
            }
        },
        // XSmall.
        xsmall: {
            range: '-480',
            // href: SITEURL + '/theme/css/style-xsmall.css',
            grid: {
                collapse: 2
            }
        }
    },
    plugins: {
        layers: {
            // Config.
            config: {
                transform: true
            },
            // Navigation Panel.
            navPanel: {
                animation: 'revealX',
                breakpoints: 'medium',
                clickToHide: true,
                height: '100%',
                hidden: true,
                html: '<div data-action="moveElement" data-args="nav"></div>',
                orientation: 'vertical',
                position: 'top-right',
                side: 'right',
                width: 250
            },
            // Navigation Button.
            navButton: {
                breakpoints: 'medium',
                height: '4em',
                html: '<span class="toggle fas fa-bars" data-action="toggleLayer" data-args="navPanel"></span>',
                position: 'top-right',
                side: 'top',
                width: '5em'
            }
        }
    }
});

/**
 * open all external links in a new window
 */
$(function() {
    $('a')
        .filter('[href^="http"], [href^="//"]')
        .not('[href*="' + window.location.host + '"]')
        .attr('rel', 'noopener noreferrer')
        .attr('target', '_blank');
});

/**
 * boostrap popover/tooltip
 */
$.fn.popover.Constructor.DEFAULTS.container = 'body';
$.fn.tooltip.Constructor.DEFAULTS.container = 'body';
$(function() {
    $('[data-toggle="popover"]').popover();
    $('[data-toggle="tooltip"]').tooltip();
});

/**
 * remove the trailing asterisk in the table of contents
 */
$(function() {
    $('.toc-href').each(function(idx, el) {
        var asterisk = '\\*';
        var regex = new RegExp(asterisk + '$');

        var $el = $(el);
        var title = $el.text();

        if (regex.test(title)) {
            title = title.replace(regex, '');
            $el.text(title).attr('title', title);
        }
    });
});
