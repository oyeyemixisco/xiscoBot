let lastAiResponse = "";
$(document).ready(function($) {
	
	// Variables declarations
	var $wrapper = $('.main-wrapper');
	var $pageWrapper = $('.page-wrapper');
	var $slimScrolls = $('.slimscroll');
	var $sidebarOverlay = $('.sidebar-overlay');
	
	// Sidebar
	var Sidemenu = function() {
		this.$menuItem = $('#sidebar-menu a');
	};

	function init() {
		var $this = Sidemenu;
		$('#sidebar-menu a').on('click', function(e) {
			if($(this).parent().hasClass('submenu')) {
				e.preventDefault();
			}
			if(!$(this).hasClass('subdrop')) {
				$('ul', $(this).parents('ul:first')).slideUp(350);
				$('a', $(this).parents('ul:first')).removeClass('subdrop');
				$(this).next('ul').slideDown(350);
				$(this).addClass('subdrop');
			} else if($(this).hasClass('subdrop')) {
				$(this).removeClass('subdrop');
				$(this).next('ul').slideUp(350);
			}
		});
		$('#sidebar-menu ul li.submenu a.active').parents('li:last').children('a:first').addClass('active').trigger('click');
	}
	// Sidebar Initiate
	init();
	
	// Sidebar overlay
	function sidebar_overlay($target) {
		if($target.length) {
			$target.toggleClass('opened');
			$sidebarOverlay.toggleClass('opened');
			$('html').toggleClass('menu-opened');
			$sidebarOverlay.attr('data-reff', '#' + $target[0].id);
		}
	}
	
	// Mobile menu sidebar overlay
	$(document).on('click', '#mobile_btn', function() {
		var $target = $($(this).attr('href'));
		sidebar_overlay($target);
		$wrapper.toggleClass('slide-nav');
		$('#chat_sidebar').removeClass('opened');
		return false;
	});
	
	// Chat sidebar overlay
	$(document).on('click', '#task_chat', function() {
		var $target = $($(this).attr('href'));
		console.log($target);
		sidebar_overlay($target);
		return false;
	});
	
	// Sidebar overlay reset
	$sidebarOverlay.on('click', function() {
		var $target = $($(this).attr('data-reff'));
		if($target.length) {
			$target.removeClass('opened');
			$('html').removeClass('menu-opened');
			$(this).removeClass('opened');
			$wrapper.removeClass('slide-nav');
		}
		return false;
	});
	
	// Password
	if($('.toggle-password').length > 0) {
		$(document).on('click', '.toggle-password', function() {
			$(this).toggleClass("feather-eye-off feather-eye");
			var input = $(".pass-input");
			if (input.attr("type") == "password") {
				input.attr("type", "text");
			} else {
				input.attr("type", "password");
			}
		});
	}
	if($('.confirm-password').length > 0) {
		$(document).on('click', '.confirm-password', function() {
			$(this).toggleClass("feather-eye-off feather-eye");
			var input = $(".pass-input-confirm");
			if (input.attr("type") == "password") {
				input.attr("type", "text");
			} else {
				input.attr("type", "password");
			}
		});
	}
	
	// Circle Progress Bar
	function animateElements() {
		$('.circle-bar2').each(function () {
			var elementPos = $(this).offset().top;
			var topOfWindow = $(window).scrollTop();
			var percent = $(this).find('.circle-graph2').attr('data-percent');
			var animate = $(this).data('animate');
			if (elementPos < topOfWindow + $(window).height() - 30 && !animate) {
				$(this).data('animate', true);
				$(this).find('.circle-graph2').circleProgress({
					value: percent / 100,
					size : 400,
					thickness: 30,
					fill: {
						color: '#2E37A4'
					}
				});
			}
		});
	}	
	
	if($('.circle-bar').length > 0) {
		animateElements();
	}
	$(window).scroll(animateElements);
	
	// Select 2
	if($('.select').length > 0) {
		$('.select').select2({
			minimumResultsForSearch: -1,
			width: '100%'
		});
	}
	
	// Floating Label
	if($('.floating').length > 0) {
		$('.floating').on('focus blur', function(e) {
			$(this).parents('.form-focus').toggleClass('focused', (e.type === 'focus' || this.value.length > 0));
		}).trigger('blur');
	}
	
	// Right Sidebar Scroll
	if($('#msg_list').length > 0) {
		$('#msg_list').slimscroll({
			height: '100%',
			color: '#878787',
			disableFadeOut: true,
			borderRadius: 0,
			size: '4px',
			alwaysVisible: false,
			touchScrollStep: 100
		});
		var msgHeight = $(window).height() - 124;
		$('#msg_list').height(msgHeight);
		$('.msg-sidebar .slimScrollDiv').height(msgHeight);
		$(window).resize(function() {
			var msgrHeight = $(window).height() - 124;
			$('#msg_list').height(msgrHeight);
			$('.msg-sidebar .slimScrollDiv').height(msgrHeight);
		});
	}
	
	// Left Sidebar Scroll
	if($slimScrolls.length > 0) {
		$slimScrolls.slimScroll({
			height: 'auto',
			width: '100%',
			position: 'right',
			size: '7px',
			color: '#ccc',
			wheelStep: 10,
			touchScrollStep: 100
		});
		var wHeight = $(window).height() - 60;
		$slimScrolls.height(wHeight);
		$('.sidebar .slimScrollDiv').height(wHeight);
		$(window).resize(function() {
			var rHeight = $(window).height() - 60;
			$slimScrolls.height(rHeight);
			$('.sidebar .slimScrollDiv').height(rHeight);
		});
	}
	
	// Page wrapper height
	var pHeight = $(window).height();
	$pageWrapper.css('min-height', pHeight);
	$(window).resize(function() {
		var prHeight = $(window).height();
		$pageWrapper.css('min-height', prHeight);
	});
	

	if($('.summernote').length > 0) {
		//var editorheight = $('.editor-card').height()-100;
        $('.summernote').summernote({
			placeholder: 'Description',
		    focus: true,
			minHeight: 100,
			disableResizeEditor: false,
			toolbar: [
				['fullscreen',],
				['fontname', ['fontname']],
				['undo'],
				['redo'],
				['datetimepicker'],
				['fontsize', ['fontsize']],
				['font', ['bold', 'italic', 'underline', 'clear']],
				['color', ['color']],
				['para', ['ul', 'ol', 'paragraph']],
				['insert', ['link', 'picture']]
			  ],
			// set focus to editable area after initializing summernote
		});
    }

	// Summernote
	
	if($('#summernote').length > 0) {
        $('#summernote').summernote({
		  height: 300,                 // set editor height
		  minHeight: null,             // set minimum height of editor
		  maxHeight: null,             // set maximum height of editor
		  focus: true                  // set focus to editable area after initializing summernote
		});
    }
	// editor
	if ($('#editor').length > 0) {
		ClassicEditor
		.create( document.querySelector( '#editor' ), {
			toolbar: {
                items: [
                    'heading', '|',
                    'fontfamily', 'fontsize', '|',
                    'alignment', '|', 
                    'fontColor', 'fontBackgroundColor', '|',
                    'bold', 'italic', 'strikethrough', 'underline', 'subscript', 'superscript', '|',
                    'link', '|',
                    'outdent', 'indent', '|',
                    'bulletedList', 'numberedList', 'todoList', '|',
                    'code', 'codeBlock', '|',
                    'insertTable', '|',
                    'uploadImage', 'blockQuote', '|',
                    'undo', 'redo'
                ],
                shouldNotGroupWhenFull: true
            }
		} )
		.then( editor => {
			window.editor = editor;
		} )
		.catch( err => {
			console.error( err.stack );
		} );
	}

	// Counter 
	
	if($('.counter').length > 0) {
		$('.counter').counterUp({
			 delay: 20,
			 time: 2000
		});
	 }
	 
	 if($('#timer-countdown').length > 0) {
		 $( '#timer-countdown' ).countdown( {
			 from: 180, // 3 minutes (3*60)
			 to: 0, // stop at zero
			 movingUnit: 1000, // 1000 for 1 second increment/decrements
			 timerEnd: undefined,
			 outputPattern: '$day Day $hour : $minute : $second',
			 autostart: true
		 });
	 }
	 
	 if($('#timer-countup').length > 0) {
		 $( '#timer-countup' ).countdown( {
			 from: 0,
			 to: 180 
		 });
	 }
	 
	 if($('#timer-countinbetween').length > 0) {
		 $( '#timer-countinbetween' ).countdown( {
			 from: 30,
			 to: 20 
		 });
	 }
	 
	 if($('#timer-countercallback').length > 0) {
		 $( '#timer-countercallback' ).countdown( {
			 from: 10,
			 to: 0,
			 timerEnd: function() {
				 this.css( { 'text-decoration':'line-through' } ).animate( { 'opacity':.5 }, 500 );
			 } 
		 });
	 }
	 
	 if($('#timer-outputpattern').length > 0) {
		 $( '#timer-outputpattern' ).countdown( {
			 outputPattern: '$day Days $hour Hour $minute Min $second Sec..',
			 from: 60 * 60 * 24 * 3
		 });
	 }

	 // Clipboard 
	
	if($('.clipboard').length > 0) {
		var clipboard = new Clipboard('.btn');
	}
	// Popover
	
	if($('.popover-list').length > 0) {
		var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
		var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
		  return new bootstrap.Popover(popoverTriggerEl)
		})
	}

	// Form Wizard
	
	$(".next").on('click', function () { // Function Runs On NEXT Button Click
		$(this).closest('.tab-pane').next().css("display" , "block").css("opacity" , "1");
		$(this).closest('.tab-pane').css({
			'display': 'none'
		});
	
	});
	$(".previous").on('click', function () { // Function Runs On NEXT Button Click
		$(this).closest('.tab-pane').prev().css("display", "block");
		$(this).closest('.tab-pane').css({
			'display': 'none'
		});
	
	});
	// Tooltip

	if($('[data-bs-toggle="tooltip"]').length > 0) {
		$('[data-bs-toggle="tooltip"]').tooltip();
	}

	if($('.custom-file-container').length > 0) {
        //First upload
        var firstUpload = new FileUploadWithPreview('myFirstImage')
        //Second upload
        var secondUpload = new FileUploadWithPreview('mySecondImage')
	}
		
	// CK Editor

	if ($('#editor').length > 0) {
		ClassicEditor
		.create( document.querySelector( '#editor' ), {
			 toolbar: {
			    items: [
			        'heading', '|',
			        'fontfamily', 'fontsize', '|',
			        'alignment', '|',
			        'fontColor', 'fontBackgroundColor', '|',
			        'bold', 'italic', 'strikethrough', 'underline', 'subscript', 'superscript', '|',
			        'link', '|',
			        'outdent', 'indent', '|',
			        'bulletedList', 'numberedList', 'todoList', '|',
			        'code', 'codeBlock', '|',
			        'insertTable', '|',
			        'uploadImage', 'blockQuote', '|',
			        'undo', 'redo'
			    ],
			    shouldNotGroupWhenFull: true
			}
		} )
		.then( editor => {
			window.editor = editor;
		} )
		.catch( err => {
			console.error( err.stack );
		} );
	}
	// Datatable
	if($('.datatable').length > 0) {
		$('.datatable').DataTable({
			"bFilter": false,
			"language": {
			paginate: {
				next: 'Next',
				previous: 'Previous'
			},
		}
		});
	}
	
	// Time
	if($('#datetimepicker3').length > 0) {
		$(function () {
			$('#datetimepicker3').datetimepicker({
				format: 'LT',
				icons: {
					up: "fas fa-angle-up",
					down: "fas fa-angle-down",
					next: 'fas fa-angle-right',
					previous: 'fas fa-angle-left'
				}
			});
		});
	}
	if($('#datetimepicker4').length > 0) {
		$(function () {
			$('#datetimepicker4').datetimepicker({
				format: 'LT',
				icons: {
					up: "fas fa-angle-up",
					down: "fas fa-angle-down",
					next: 'fas fa-angle-right',
					previous: 'fas fa-angle-left'
				}
			});
		});
	}
	
	
	
	// slick
	if($('.center').length > 0) {
		$('.center').slick({
		  centerMode: true,
		  arrows: false,
		  centerPadding: '30px',
		  slidesToShow: 3,
		  responsive: [
			{
			  breakpoint: 768,
			  settings: {
				arrows: false,
				centerMode: true,
				centerPadding: '40px',
				slidesToShow: 3
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				arrows: false,
				centerMode: true,
				centerPadding: '40px',
				slidesToShow: 3
			  }
			}
		  ]
		});
	}
	
	// Bootstrap Tooltip
	if($('[data-toggle="tooltip"]').length > 0) {
		$('[data-toggle="tooltip"]').tooltip();
	}
	
	// Mobile Menu
	$(document).on('click', '#open_msg_box', function() {
		$wrapper.toggleClass('open-msg-box');
		return false;
	});
	
	// Lightgallery
	if($('#lightgallery').length > 0) {
		$('#lightgallery').lightGallery({
			thumbnail: true,
			selector: 'a'
		});
	}
	
	// Incoming call popup
	if($('#incoming_call').length > 0) {
		$('#incoming_call').modal('show');
	}
	
	// JQuery counterUp

	if($('.dash-count .counter-up').length > 0) {
		$('.dash-count .counter-up').counterUp({
            delay: 15,
            time: 1500
        });
	}
	
	// Summernote
	if($('.summernote').length > 0) {
		$('.summernote').summernote({
			height: 200,
			minHeight: null,
			maxHeight: null,
			focus: false
		});
	}
	
	// Check all email
	$(document).on('click', '#check_all', function() {
		$('.checkmail').click();
		return false;
	});
	if($('.checkmail').length > 0) {
		$('.checkmail').each(function() {
			$(this).on('click', function() {
				if($(this).closest('tr').hasClass('checked')) {
					$(this).closest('tr').removeClass('checked');
				} else {
					$(this).closest('tr').addClass('checked');
				}
			});
		});
	}
	
	// Mail important
		$(document).on('click', '.mail-important', function() {
		$(this).find('i.fa').toggleClass('fa-star').toggleClass('fa-star-o');
	});
	
	// Dropfiles
	if($('#drop-zone').length > 0) {
		var dropZone = document.getElementById('drop-zone');
		var uploadForm = document.getElementById('js-upload-form');
		var startUpload = function(files) {
			console.log(files);
		};
		uploadForm.addEventListener('submit', function(e) {
			var uploadFiles = document.getElementById('js-upload-files').files;
			e.preventDefault();
			startUpload(uploadFiles);
		});
		dropZone.ondrop = function(e) {
			e.preventDefault();
			this.className = 'upload-drop-zone';
			startUpload(e.dataTransfer.files);
		};
		dropZone.ondragover = function() {
			this.className = 'upload-drop-zone drop';
			return false;
		};
		dropZone.ondragleave = function() {
			this.className = 'upload-drop-zone';
			return false;
		};
	}
	
	// Small Sidebar
	if(screen.width >= 992) {
		$(document).on('click', '#toggle_btn', function() {
			if($('body').hasClass('mini-sidebar')) {
				$('body').removeClass('mini-sidebar');
				$('.subdrop + ul').slideDown();
			} else {
				$('body').addClass('mini-sidebar');
				$('.subdrop + ul').slideUp();
			}
			return false;
		});
		$(document).on('mouseover', function(e) {
			e.stopPropagation();
			if($('body').hasClass('mini-sidebar') && $('#toggle_btn').is(':visible')) {
				var targ = $(e.target).closest('.sidebar').length;
				if(targ) {
					$('body').addClass('expand-menu');
					$('.subdrop + ul').slideDown();
				} else {
					$('body').removeClass('expand-menu');
					$('.subdrop + ul').slideUp();
				}
				return false;
			}
		});
	}
	if ($('[data-feather]').length > 0) {
		feather.replace();
		}
	// Checkbox Select
	
		$('.app-listing .selectBox').on("click", function() {
			$(this).parent().find('#checkBoxes').fadeToggle();
			$(this).parent().parent().siblings().find('#checkBoxes').fadeOut();
		});

		$('.invoices-main-form .selectBox').on("click", function() {
			$(this).parent().find('#checkBoxes-one').fadeToggle();
			$(this).parent().parent().siblings().find('#checkBoxes-one').fadeOut();
		});
	// Invoices Checkbox Show

		$(function() {
			$("input[name='invoice']").click(function() {
				if ($("#chkYes").is(":checked")) {
					$("#show-invoices").show();
				} else {
					$("#show-invoices").hide();
				}
			});
		});
		// Invoices Table Add More
	
		$(".add-table-items").on('click','.remove-btn', function () {
			$(this).closest('.add-row').remove();
			return false;
		});
		 // Editor
		if ($('#editor').length > 0) {
			ClassicEditor
			.create( document.querySelector( '#editor' ), {
				toolbar: [  'bold', 'italic', 'link' ]
			} )
			.then( editor => {
				window.editor = editor;
			} )
			.catch( err => {
				console.error( err.stack );
			} );
		}
		$(document).on("click",".add-links1",function () {
			var experiencecontent = '<div class="links-cont">' +
				'<div class="service-amount">' +
					'<a href="#" class="service-trash1"><i class="fa fa-minus-circle me-1"></i>Service Charge</a> <span>$ 4</span' +
				'</div>' +
			'</div>';
			
			$(".links-info-one").append(experiencecontent);
			return false;
		});
		$(".links-info-one").on('click','.service-trash1', function () {
			$(this).closest('.links-cont').remove();
			return false;
		});
		
		
		 $(".links-info-discount").on('click','.service-trash-one', function () {
			$(this).closest('.links-cont-discount').remove();
			return false;
		});
		// Logo Hide Btn

		$(document).on("click",".logo-hide-btn",function () {
			$(this).parent().hide();
		});
		
		$(document).on("click",".add-btns",function () {
			var experiencecontent = '<tr class="add-row">' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td class="add-remove text-end">' +
				' <a href="javascript:void(0);" class="add-btns me-2"><i class="fas fa-plus-circle"></i></a> ' +
				' <a href="#" class="copy-btn me-2"><i class="fas fa-copy"></i></a>' +
				'<a href="javascript:void(0);" class="remove-btn"><i class="fa fa-trash-alt"></i></a>' +
				'</td>' +
			'</tr>';
			
			$(".add-table-items").append(experiencecontent);
			return false;
		});
		$(document).on("click",".add-links",function () {
			var experiencecontent = '<div class="links-info"><div class="row form-row links-cont">' +
					'<div class="input-block form-placeholder d-flex">' +
						'<button class="btn social-icon"><i class="feather-github"></i></button>' +
						'<input type="text" class="form-control" placeholder="Social Link">' +
						'<a href="#" class="btn trash">' +
						'<i class="feather-trash-2"></i>' +
						'</a>'+
					'</div>' +
				'</div>' +
			'</div>';
			
			$(".settings-form").append(experiencecontent);
			return false;
		});
		$(".settings-form").on('click','.trash', function () {
			$(this).closest('.links-cont').remove();
			return false;
		});
});



document.addEventListener('DOMContentLoaded', () => {
  const video = document.getElementById('loginVideo');
  const muteBtn = document.getElementById('muteBtn');

  // ✅ If not on the login page, don't run this code
  if (!video || !muteBtn) return;

  function syncMuteUI() {
    muteBtn.classList.toggle('muted', video.muted);
    muteBtn.setAttribute('aria-label', video.muted ? 'Unmute video' : 'Mute video');
  }

  syncMuteUI();

  muteBtn.addEventListener('click', () => {
    video.muted = !video.muted;
    syncMuteUI();
  });

  video.addEventListener('volumechange', syncMuteUI);
});



document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('darkModeToggle');
    const body = document.body;

    // 1. Check for saved preference
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-theme');
    }

    // 2. Add click event
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            body.classList.toggle('dark-theme');
            
            // 3. Save preference
            if (body.classList.contains('dark-theme')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }
});

const textarea = document.getElementById('chatInput');
const sendBtn = document.getElementById('sendBtn');

const welcomeSection = document.getElementById('welcomeSection');
const chatMessages = document.getElementById('chatMessages');
const inputWrapper = document.getElementById('inputWrapper');
const messageList = document.getElementById('messageList');
const chatInput = document.getElementById('chatInput');


textarea.addEventListener('input', function() {
    // 1. Auto-expand height
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';

    // 2. Toggle button color based on content
    if (this.value.trim().length > 0) {
        sendBtn.classList.add('active');
    } else {
        sendBtn.classList.remove('active');
    }
});


async function sendMessage() {
    const text = chatInput.value.trim();
    if (!text) return;

    // 1. UI Transition (Welcome -> Chat)
    if (window.getComputedStyle(welcomeSection).display !== 'none') {
        welcomeSection.style.display = 'none';
        chatMessages.style.display = 'block';
        inputWrapper.classList.remove('initial-state');
        inputWrapper.classList.add('chatting-mode');

		document.body.classList.add('chatting-mode-active');
    }

    // 2. Add User Message to UI
    const userWrapper = document.createElement('div');
    userWrapper.className = 'chat-message-wrapper user-side';
    userWrapper.innerHTML = `
        <div class="avatar"><img src="/static/img/user1.jpg"></div>
        <div class="message user-msg">${text}</div>
    `;
    messageList.appendChild(userWrapper);

    // 3. Clear and Reset Input
    chatInput.value = "";
    chatInput.style.height = 'auto';
    sendBtn.classList.remove('active');
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });

    // 4. Show AI "Typing" Bubble
    const aiWrapper = document.createElement('div');
    aiWrapper.className = 'chat-message-wrapper ai-side';
    aiWrapper.innerHTML = `
        <div class="avatar"><img src="/static/xiscoB.png"></div>
        <div class="message ai-msg">
            <div class="typing-dots"><span></span><span></span><span></span></div>
        </div>
    `;
    messageList.appendChild(aiWrapper);

    try {
        // 5. POST request to Flask
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });

        const data = await response.json();

        // 6. Replace dots with real AI text
        const aiMessageDiv = aiWrapper.querySelector('.ai-msg');
        aiMessageDiv.innerHTML = marked.parse(data.response);

		lastAiResponse = data.response;

		speakText(data.response);

    } catch (error) {
        aiWrapper.querySelector('.ai-msg').innerText = "Connection error. Please try again.";
    }

    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
}

// Helper function to toggle the text
function toggleMessage(button) {
    const textDiv = button.previousElementSibling;
    const isCollapsed = textDiv.classList.contains('collapsed');

    if (isCollapsed) {
        textDiv.classList.remove('collapsed');
        textDiv.style.maskImage = 'none'; 
        textDiv.style.webkitMaskImage = 'none';
        button.innerHTML = 'Show less <i class="fa fa-angle-up"></i>';
    } else {
        textDiv.classList.add('collapsed');
        textDiv.style.maskImage = 'linear-gradient(180deg, black 50%, transparent 100%)';
        textDiv.style.webkitMaskImage = 'linear-gradient(180deg, black 50%, transparent 100%)';
        button.innerHTML = 'Expand text <i class="fa fa-angle-down"></i>';
    }
}


// Attach to Button
sendBtn.addEventListener('click', sendMessage);

// Attach to Enter Key
chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// TypeWriter
const textElement = document.getElementById("typewriter");
const phrases = [
    "I speak english?",      // English
    "Je parle français",   // French
    "Yo hablo español"       // Spanish
];

let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typeSpeed = 100;

function type() {
    const currentPhrase = phrases[phraseIndex];
    
    if (isDeleting) {
        // Remove characters
        textElement.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        typeSpeed = 50; // Deleting is usually faster
    } else {
        // Add characters
        textElement.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        typeSpeed = 100;
    }

    // Logic for switching between typing and deleting
    if (!isDeleting && charIndex === currentPhrase.length) {
        // Pause at the end of the phrase
        isDeleting = true;
        typeSpeed = 2000; // Wait 2 seconds before deleting
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typeSpeed = 500; // Wait a bit before starting next phrase
    }

    setTimeout(type, typeSpeed);
}

window.speechSynthesis.onvoiceschanged = () => {
  console.log("Voices loaded:", window.speechSynthesis.getVoices().length);
};

// Start the animation when the page loads
document.addEventListener("DOMContentLoaded", () => {
    if (textElement) type();
});

let isVoiceEnabled = false;
let VOICES = [];

function loadVoices() {
  VOICES = window.speechSynthesis.getVoices() || [];
}

function pickVoice() {
  // Prefer good Mac voices if available
  const preferredNames = ["Samantha", "Daniel", "Victoria", "Alex"];
  for (const name of preferredNames) {
    const v = VOICES.find(x => x.name && x.name.includes(name));
    if (v) return v;
  }
  // else pick an English voice
  const en = VOICES.find(x => (x.lang || "").toLowerCase().startsWith("en"));
  return en || VOICES[0] || null;
}

function setupVoice() {
  const voiceToggle = document.getElementById('voiceToggle');
  const voiceIcon = document.getElementById('voiceIcon');
  if (!voiceToggle || !voiceIcon) return;

  if (voiceToggle.dataset.bound === "1") return;
  voiceToggle.dataset.bound = "1";

  voiceToggle.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();

    isVoiceEnabled = !isVoiceEnabled;
    console.log("Voice enabled:", isVoiceEnabled, "voices:", speechSynthesis.getVoices().length);

    if (isVoiceEnabled) {
      voiceIcon.className = "fa fa-volume-up";
      voiceIcon.style.color = "#2e0074";

      // ✅ speak last AI response immediately
      if (lastAiResponse) speakText(lastAiResponse);
    } else {
      voiceIcon.className = "fa fa-volume-mute";
      voiceIcon.style.color = "black";
      speechSynthesis.cancel();
    }
  });
}


document.addEventListener("DOMContentLoaded", setupVoice);


function speakText(text) {
  console.log("speakText called. isVoiceEnabled =", isVoiceEnabled);
  if (!isVoiceEnabled) return;
  if (!text || !text.trim()) return;

  // Stop any ongoing speech
  window.speechSynthesis.cancel();

  const u = new SpeechSynthesisUtterance(text);

  // Try to pick a good Mac voice (fallback if not found)
  const voices = window.speechSynthesis.getVoices();
  const preferred =
    voices.find(v => v.name.includes("Samantha")) ||
    voices.find(v => v.name.includes("Daniel")) ||
    voices.find(v => v.lang && v.lang.toLowerCase().startsWith("en")) ||
    voices[0];

  if (preferred) u.voice = preferred;

  u.rate = 1;
  u.pitch = 1;
  u.volume = 1;

  u.onstart = () => console.log("Speech started:", u.voice?.name);
  u.onend = () => console.log("Speech ended");
  u.onerror = (e) => console.error("Speech error:", e);

  // ✅ Mac/Chrome reliability trick: delay slightly after cancel()
  setTimeout(() => window.speechSynthesis.speak(u), 80);
}


// Init once
document.addEventListener("DOMContentLoaded", () => {
  setupVoice();
});

// Initialization
document.addEventListener("DOMContentLoaded", () => {
    setupVoice();
    // Warm up voices
    window.speechSynthesis.getVoices();
});