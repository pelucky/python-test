" Load pathogen to manage plugins
call pathogen#runtime_append_all_bundles()
call pathogen#helptags()
call pathogen#infect()
" enable filetype dectection and ft specific plugin/indent
"filetype on  
"filetype plugin on
filetype plugin indent on

" enable syntax hightlight and completion 
syntax enable
syntax on

" Change by pel
" 插入匹配括号
"inoremap ( ()<LEFT>
"inoremap [ []<LEFT>
"inoremap { {}<LEFT>
"inoremap < <><LEFT>
"inoremap " ""<LEFT>
"inoremap ' ''<LEFT>
" 
" color theme
"color bensday

" highlight current line
au WinLeave * set nocursorline nocursorcolumn
au WinEnter * set cursorline cursorcolumn
set cursorline cursorcolumn"

" search operations
set incsearch
"set highlight 	" conflict with highlight current line
set ignorecase
set smartcase

" paste codes
set nopaste 
set pastetoggle=<F10>

set history=1000
set nocompatible
set t_Co=256 " Explicitly tell vim that the terminal has 256 colors"
set number      " show linenumber
set confirm 	" prompt when existing from an unsaved file
"set ruler
set showcmd 	" Show (partial) command in status line
set mouse=a " use mouse in all modes 
set report=0 " always report number of lines changed"
set backspace=indent,eol,start 	" More powerful backspacing

" Default Indentation
set autoindent
set smartindent     " indent when
set tabstop=8       " tab width
set softtabstop=4   " backspace & 
set shiftwidth=4    " indent width
"set textwidth=79
set expandtab       " expand tab to space
autocmd FileType html,haml,sass,scss,ruby,javascript,php,css,java,c,c++
set tabstop=4 shiftwidth=2 softtabstop=2

" javascript
" nmap <silent> <leader>js :call g:Jsbeautify()<cr>
nnoremap <F4> :call g:Jsbeautify()<CR>
let mapleader=","

"pythoncomplete
autocmd FileType python set textwidth=0
autocmd FileType python set omnifunc=pythoncomplete#Complete  

" JQuery syntax support
autocmd Syntax javascript set syntax=jquery
au BufRead,BufNewFile *.js set syntax=jquery

"设置字典 ~/.vim/dict/javascript.dict是字典文件的路径
autocmd FileType <span class="hilite">javascript</span> set dictionary=~/.<span class="hilite">vim</span>/dict/javascript.dict
"
" Keybindings for plugin toggle
"nmap <F4> :IndentGuidesToggle<cr>
nmap <F5> :TagbarToggle<cr>
nmap <F6> :NERDTreeToggle<cr>
" easier navigation between split windows
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l

" Tagbar
let g:tagbar_left=1
let g:tagbar_width=30
let g:tagbar_autofocus = 1
let g:tagbar_sort = 0 

" Nerd Tree 
let NERDChristmasTree=0
let NERDTreeWinSize=30
let NERDTreeChDirMode=2
let NERDTreeIgnore=['\.vim$', '\~$', '\.pyc$', '\.swp$']
let NERDTreeSortOrder=['^__\.py$', '\/$', '*', '\.swp$',  '\~$']
let NERDTreeShowBookmarks=1
let NERDTreeWinPos = "left"

" ZenCoding
let g:user_zen_expandabbr_key='<C-j>'

" Indent guides (default toggle key is <leader>ig)
"let g:indent_guides_auto_colors=0
"let g:indent_guides_start_level=2 
"let g:indent_guides_guide_size=1
"autocmd VimEnter,Colorscheme * :hi IndentGuidesOdd  ctermbg=239
"autocmd VimEnter,Colorscheme * :hi IndentGuidesEven ctermbg=242

" NeoComplCache
set completeopt=longest,menu
let g:neocomplcache_enable_at_startup=1
"let g:neoComplcache_disableautocomplete=1
let g:neocomplcache_enable_smart_case=1
let g:neocomplcache_min_syntax_length = 3
imap <C-k> <Plug>(neocomplcache_snippets_force_expand)
smap <C-k> <Plug>(neocomplcache_snippets_force_expand)
"imap <C-l> <Plug>(neocomplcache_snippets_expand)
"smap <C-l> <Plug>(neocomplcache_snippets_expand)
"imap <C-t> <Plug>(neocomplcache_snippets_jump)
"smap <C-t> <Plug>(neocomplcache_snippets_jump)
imap <C-l> <Plug>(neocomplcache_snippets_force_jump)
smap <C-l> <Plug>(neocomplcache_snippets_force_jump)

" SuperTab
let g:SuperTabDefaultCompletionType="<c-n>"
"let g:SuperTabDefaultCompletionType="<C-X><C-U>"
"let g:SuperTabDefaultCompletionType="context"

" 
set laststatus=2 " Always show the statusline"

" eggcache vim
:command W w
:command WQ wq
:command Wq wq
:command Q q
:command Qa qa
:command QA qa

" show syntax highlighting groups for word under cursor
nmap <C-P> :call <SID>SynStack()<CR>
function! <SID>SynStack()
  if !exists("*synstack")
    return
  endif
  echo map(synstack(line('.'), col('.')), 'synIDattr(v:val, "name")')
endfunc

"javacomplete
if has("autocmd")
  autocmd Filetype java setlocal omnifunc=javacomplete#Complete
endif
setlocal completefunc=javacomplete#CompleteParamsInfo
inoremap<buffer> <C-X><C-U> <C-X><C-U><C-P> 
inoremap <buffer> <C-S-Space> <C-X><C-U><C-P>
