html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>الرحلة الشاملة في رياضيات البكالوريا: نحو 20/20</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;700;900&amp;display=swap" rel="stylesheet">
<style>
:root{--page:#EEF1F6;--surface:#fff;--text:#1B2230;--text2:#55607A;--line:rgba(27,34,48,.14);--accent:#185FA5;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--page:#12151B;--surface:#1C212B;--text:#E8ECF4;--text2:#A5AEC2;--line:rgba(232,236,244,.18);--accent:#85B7EB}}
:root[data-theme="dark"]{--page:#12151B;--surface:#1C212B;--text:#E8ECF4;--text2:#A5AEC2;--line:rgba(232,236,244,.18);--accent:#85B7EB}
html{scroll-padding-top:env(safe-area-inset-top,0px);scroll-behavior:smooth}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--text);font-family:"Cairo",system-ui,"Segoe UI",Tahoma,sans-serif;line-height:1.75;font-size:16px}
main{max-width:580px;margin:0 auto;padding:24px 16px 48px}
h1{font-size:27px;font-weight:900;margin:0 0 6px;line-height:1.4;background:linear-gradient(135deg,var(--accent),#7F77DD);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.sub{margin:0 0 20px;color:var(--text2);font-size:15px;font-weight:500}
.prog{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin-bottom:20px;box-shadow:0 4px 20px rgba(0,0,0,.03)}
.prog-top{display:flex;justify-content:space-between;align-items:center;gap:8px;font-size:14px;margin-bottom:8px;font-weight:700}
.bar{height:8px;border-radius:4px;background:var(--line);overflow:hidden}
#pf{height:100%;width:0;background:linear-gradient(90deg,var(--accent),#7F77DD);border-radius:4px;transition:width .5s cubic-bezier(.4,0,.2,1)}
button{font-family:inherit;font-size:inherit}
#all{background:transparent;color:var(--text);border:1px solid var(--line);border-radius:8px;padding:3px 12px;font-size:13px;cursor:pointer;font-weight:700}
button:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.k{--bg:var(--lb);--ln:var(--ll);--tx:var(--lt)}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) .k{--bg:var(--db);--ln:var(--dl);--tx:var(--dt)}}
:root[data-theme="dark"] .k{--bg:var(--db);--ln:var(--dl);--tx:var(--dt)}
.cb{--lb:#E6F1FB;--ll:#185FA5;--lt:#0C447C;--db:#0C447C;--dl:#85B7EB;--dt:#B5D4F4}
.ct{--lb:#E1F5EE;--ll:#0F6E56;--lt:#085041;--db:#085041;--dl:#5DCAA5;--dt:#9FE1CB}
.cp{--lb:#FBEAF0;--ll:#993556;--lt:#72243E;--db:#72243E;--dl:#ED93B1;--dt:#F4C0D1}
.cu{--lb:#EEEDFE;--ll:#534AB7;--lt:#3C3489;--db:#3C3489;--dl:#AFA9EC;--dt:#CECBF6}
.ca{--lb:#FAEEDA;--ll:#854F0B;--lt:#633806;--db:#633806;--dl:#EF9F27;--dt:#FAC775}
.cg{--lb:#EAF3DE;--ll:#3B6D11;--lt:#27500A;--db:#27500A;--dl:#97C459;--dt:#C0DD97}
.cc{--lb:#FAECE7;--ll:#993C1D;--lt:#712B13;--db:#712B13;--dl:#F0997B;--dt:#F5C4B3}
.cz{--lb:#F3E8FF;--ll:#7C3AED;--lt:#5B21B6;--db:#5B21B6;--dl:#A78BFA;--dt:#E9D5FF}
.cy{--lb:#E9E8E2;--ll:#5F5E5A;--lt:#2C2C2A;--db:#2E2E2C;--dl:#B4B2A9;--dt:#D3D1C7}

.qb{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.qq{font-size:16px;font-weight:700;margin:0 0 12px;color:var(--text)}
.qa{display:block;width:100%;text-align:start;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--text);cursor:pointer;margin:6px 0;font-size:15px;transition:all .2s}
.qa:active{transform:scale(.97)}
.qa.correct{background:#E1F5EE;border-color:#0F6E56;color:#085041}
.qa.wrong{background:#FAECE7;border-color:#993C1D;color:#712B13}
.qe{margin-top:8px;font-size:14px;color:var(--text2)}
.st{display:grid;grid-template-columns:40px minmax(0,1fr);gap:12px;margin-bottom:16px}
.rl{position:relative;display:flex;justify-content:center;align-items:flex-start}
.rl::before{content:"";position:absolute;top:44px;bottom:-16px;left:calc(50% - 1px);border-left:2px dashed var(--ln)}
.st.last .rl::before{display:none}
.nm{width:40px;height:40px;border-radius:50%;background:var(--ln);color:var(--bg);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:17px;box-shadow:0 3px 10px rgba(0,0,0,.1)}
.cd{background:var(--bg);border:1px solid var(--ln);border-radius:14px;color:var(--tx);box-shadow:0 4px 16px rgba(0,0,0,.04)}
.hd{display:flex;align-items:center;gap:10px;width:100%;padding:12px 16px;background:transparent;border:none;color:var(--tx);text-align:start;cursor:pointer;min-height:58px;border-radius:14px}
.hd .tt{flex:1;min-width:0}
.hd b{display:block;font-size:18px;font-weight:700;line-height:1.4}
.hd small{display:block;font-size:13px;color:var(--ln);line-height:1.4;font-weight:500}
.chev{font-size:18px;color:var(--ln)}
@media(prefers-reduced-motion:no-preference){.chev{transition:transform .25s}}
.st:not(.closed) .chev{transform:rotate(180deg)}
.bd{padding:0 16px 16px;font-size:15px}
.st.closed .bd{display:none}
.bd p{margin:6px 0}
.t{display:inline-block;background:var(--ln);color:var(--bg);font-size:13px;font-weight:700;padding:2px 12px;border-radius:8px;margin:12px 0 4px}
.f{direction:ltr;text-align:center;background:var(--surface);border:1px solid var(--ln);border-radius:10px;padding:8px 10px;margin:8px 0;color:var(--text);font-family:"Cambria Math","Times New Roman",serif;font-size:17px;line-height:1.6;overflow-x:auto;box-shadow:inset 0 1px 3px rgba(0,0,0,.03)}
.m{direction:ltr;unicode-bidi:isolate;display:inline-block;font-family:"Cambria Math","Times New Roman",serif;font-size:16px;font-weight:bold}
.s{display:flex;gap:10px;margin:8px 0;align-items:flex-start}
.n{flex:none;width:24px;height:24px;border-radius:50%;background:var(--ln);color:var(--bg);font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:4px}
.s>div{flex:1;min-width:0}
.mk{margin-top:12px;background:transparent;color:var(--tx);border:1px solid var(--ln);border-radius:9px;padding:7px 16px;cursor:pointer;font-size:14px;font-weight:700}
.mk[aria-pressed="true"]{background:var(--ln);color:var(--bg)}
.sec{margin:36px 0 14px;font-size:22px;font-weight:900;line-height:1.5;letter-spacing:-0.5px}
.ex{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:16px;margin-bottom:14px;font-size:15px;box-shadow:0 4px 16px rgba(0,0,0,.03)}
.ex h3{margin:0 0 8px;font-size:18px;font-weight:700;color:var(--accent)}
.ex ol{margin:8px 0;padding-inline-start:24px}
.ex li{margin:4px 0}
summary{cursor:pointer;color:var(--accent);font-weight:700;margin-top:10px;display:inline-block}
.sol{margin-top:8px;border-top:1px solid var(--line);padding-top:8px}
.vh{font-weight:700;margin:18px 0 6px;color:var(--text)}
.vd a{display:block;padding:12px 14px;border:1px solid var(--line);border-radius:12px;margin:8px 0;color:var(--text);text-decoration:none;background:var(--surface);font-size:15px;transition:all .2s}
.vd a:hover{border-color:var(--accent);transform:translateX(-3px)}
.vd a small{display:block;color:var(--text2);font-size:13px;margin-top:2px}
a:focus-visible,summary:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.hero{position:relative;margin-bottom:6px}
.hero h1,.hero .sub{position:relative;z-index:1}
.sym{position:absolute;font-family:"Cambria Math","Times New Roman",serif;font-size:36px;color:var(--text2);opacity:.18;pointer-events:none;user-select:none}
.pm{margin:8px 0 0;font-size:14px;color:var(--text2);font-weight:600}
.cf{position:fixed;width:8px;height:12px;border-radius:2px;pointer-events:none;z-index:70}
#toast{position:fixed;left:50%;bottom:calc(20px + env(safe-area-inset-bottom,0px));transform:translate(-50%,20px);background:var(--text);color:var(--page);padding:12px 22px;border-radius:999px;font-size:15px;font-weight:700;opacity:0;pointer-events:none;transition:opacity .25s,transform .25s;z-index:60;max-width:calc(100% - 32px);text-align:center;box-shadow:0 10px 30px rgba(0,0,0,.2)}
#toast.on{opacity:1;transform:translate(-50%,0)}
.credit{margin-top:40px;padding:24px 16px 12px;border-top:1px solid var(--line);text-align:center}
.credit p{margin:3px 0;color:var(--text2);font-size:14px}
.credit .who{color:var(--text);font-weight:900;font-size:18px}
.ig{display:inline-flex;align-items:center;gap:8px;margin-top:16px;padding:10px 24px;background:#C13584;color:#fff;border-radius:999px;text-decoration:none;font-weight:700;font-size:15px;box-shadow:0 4px 15px rgba(193,53,132,.3)}
.ig:hover{background:#A92A72}
.mk:active,#all:active,.ig:active{transform:scale(.97)}
@media(hover:hover){.cd:hover,.ig:hover{transform:translateY(-2px)}}
@media(prefers-reduced-motion:no-preference){
@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
@keyframes fl{from{transform:translateY(0) rotate(-6deg)}to{transform:translateY(-12px) rotate(6deg)}}
@keyframes ring{0%{box-shadow:0 0 0 0 var(--ln)}100%{box-shadow:0 0 0 14px transparent}}
@keyframes opn{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:none}}
.st{animation:rise .5s ease-out both}
.sym{animation:fl 4.5s ease-in-out infinite alternate}
.st.next .nm{animation:ring 1.8s ease-out infinite}
.st:not(.closed) .bd{animation:opn .25s ease-out}
.cd,.ig,.mk,#all{transition:transform .15s,background-color .15s}
}
.tm{display:flex;align-items:center;gap:8px;margin-top:12px;padding-top:12px;border-top:1px solid var(--line)}
.tl{flex:1;font-size:14px;color:var(--text2);font-weight:700}
.td{font-size:22px;font-weight:900;font-variant-numeric:tabular-nums}
.tm.brk .td,.tm.brk .tl{color:var(--accent)}
.tm button{background:transparent;color:var(--text);border:1px solid var(--line);border-radius:8px;padding:3px 12px;font-size:13px;cursor:pointer;font-weight:700}
.tm button:active{transform:scale(.97)}
.level-btn{background:transparent;color:var(--tx);border:1px solid var(--ln);border-radius:8px;padding:6px 10px;cursor:pointer;font-size:13px;font-weight:700;flex:1;text-align:center;transition:all .2s}
.level-btn.active{background:var(--ln);color:var(--bg)}
</style>
</head>
<body>
<main>
<div class="hero">
<span class="sym" aria-hidden="true" style="left:4px;top:0;animation-duration:4s">∫</span>
<span class="sym" aria-hidden="true" style="left:52px;top:34px;animation-duration:5s;animation-delay:-1s">z</span>
<span class="sym" aria-hidden="true" style="left:8px;top:62px;animation-duration:4.5s;animation-delay:-2s">u<sub>n</sub></span>
<span class="sym" aria-hidden="true" style="left:78px;top:4px;animation-duration:5.5s;animation-delay:-3s">→</span>
<h1>برنامج الرياضيات للباكالوريا: رحلتك نحو 20/20</h1>
<p class="sub">محطات متكاملة تغطي كافة وحدات البرنامج الرسمي (شعب علمية وتقنية) بترتيب احترافي دقيق.</p>
</div>
<div class="prog">
<div class="prog-top"><span id="pt">أتقنت 0 من 8 محطات</span><button id="all">فتح الكل</button></div>
<div class="bar"><div id="pf"></div></div>
<p id="pm" class="pm"></p>
<p id="qp" class="pm"></p>
<div class="tm"><span id="tl" class="tl">وقت المراجعة</span><span id="td" class="td" dir="ltr">25:00</span><button id="tg">ابدأ</button><button id="tr">إعادة</button></div>
</div>

<!-- المحطة 1: الدوال الأسية واللوغاريتمية -->
<div class="st k cb">
<div class="rl"><div class="nm">1</div></div>
<div class="cd">
<button class="hd" aria-expanded="true"><span class="tt"><b>الدوال الأسية واللوغاريتمية</b><small>الدوال المرجعية، النهايات، والاستمرارية</small></span><span class="chev" aria-hidden="true">▾</span></button>
<div class="bd">
<span class="t">الدالة الأسية النيبرية e^x</span>
<div class="f">e<sup>0</sup> = 1 , e<sup>a+b</sup> = e<sup>a</sup>·e<sup>b</sup> , ln(e<sup>x</sup>) = x</div>
<span class="t">الدالة اللوغاريتمية النيبرية ln(x)</span>
<div class="f">ln(1) = 0 , ln(a·b) = ln(a) + ln(b) , e<sup>ln(x)</sup> = x (x &gt; 0)</div>
<span class="t">نهايات شهيرة</span>
<div class="f">lim<sub>x→+∞</sub> (e<sup>x</sup> / x<sup>n</sup>) = +∞ , lim<sub>x→+∞</sub> (ln(x) / x) = 0</div>
<div class="s"><span class="n">1</span><div>دراسة الاتجاه بحساب المشتقة <span class="m">f'(x)</span> وإشارة البسط.</div></div>
<div class="s"><span class="n">2</span><div>المستقيمات المقاربة: عمودية، أفقية، ومائلة بجوار <span class="m">±∞</span>.</div></div>
</div></div></div>

<!-- المحطة 2: الحساب التكاملي والدوال الأصلية -->
<div class="st k ct closed">
<div class="rl"><div class="nm">2</div></div>
<div class="cd">
<button class="hd" aria-expanded="false"><span class="tt"><b>الحساب التكاملي والدوال الأصلية</b><small>حساب المساحات وحجم الدوران</small></span><span class="chev" aria-hidden="true">▾</span></button>
<div class="bd">
<span class="t">تعريف التكامل</span>
<div class="f">∫<sub>a</sub><sup>b</sup> f(x) dx = F(b) - F(a)</div>
<p>حيث <span class="m">F</span> دالة أصلية لـ <span class="m">f</span> على المجال <span class="m">[a, b]</span>.</p>
<span class="t">خواص التكامل</span>
<div class="f">∫<sub>a</sub><sup>b</sup> f(x) dx = - ∫<sub>b</sub><sup>a</sup> f(x) dx , ∫<sub>a</sub><sup>c</sup> = ∫<sub>a</sub><sup>b</sup> + ∫<sub>b</sub><sup>c</sup></div>
<span class="t">حساب المساحات</span>
<div class="f">A = ∫<sub>a</sub><sup>b</sup> |f(x) - g(x)| dx · (unit_area)</div>
<span class="t">المجال بالتجزئة (Integration by Parts)</span>
<div class="f">∫<sub>a</sub><sup>b</sup> u(x)v'(x) dx = [u(x)v(x)]<sub>a</sub><sup>b</sup> - ∫<sub>a</sub><sup>b</sup> u'(x)v(x) dx</div>
</div></div></div>

<!-- المحطة 3: المتتاليات العددية -->
<div class="st k cp closed">
<div class="rl"><div class="nm">3</div></div>
<div class="cd">
<button class="hd" aria-expanded="false"><span class="tt"><b>المتتاليات العددية</b><small>الحسابية، الهندسية، والبرهان بالتراجع</small></span><span class="chev" aria-hidden="true">▾</span></button>
<div class="bd">
<span class="t">المتتالية الحسابية والهندسية</span>
<div class="f">u<sub>n</sub> = u<sub>0</sub> + n·r , v<sub>n</sub> = v<sub>0</sub>·q<sup>n</sup></div>
<span class="t">المتتالية المساعدة a·u + b</span>
<div class="f">α = b / (1 - a) , v<sub>n</sub> = u<sub>n</sub> - α</div>
<span class="t">البرهان بالتراجع</span>
<div class="s"><span class="n">1</span><div>التحقق من صحة الخاصية عند الحد الابتدائي <span class="m">P(0)</span>.</div></div>
<div class="s"><span class="n">2</span><div>الوراثة: نفرض صحة <span class="m">P(n)</span> ونبرهن صحة <span class="m">P(n+1)</span>.</div></div>
</div></div></div>

<!-- المحطة 4: الأعداد المركبة -->
<div class="st k cu closed">
<div class="rl"><div class="nm">4</div></div>
<div class="cd">
<button class="hd" aria-expanded="false"><span class="tt"><b>الأعداد المركبة</b><small>الشكل الجبري، الأسي، والتحويلات النقطية</small></span><span class="chev" aria-hidden="true">▾</span></button>
<div class="bd">
<span class="t">الشكل الجبري والأسي</span>
<div class="f">z = x + iy = |z|e<sup>iθ</sup> , |z| = √(x<sup>2</sup> + y<sup>2</sup>)</div>
<span class="t">دستور موافر وأويلر</span>
<div class="f">(e<sup>iθ</sup>)<sup>n</sup> = e<sup>inθ</sup> , cos(θ) = (e<sup>iθ</sup> + e<sup>-iθ</sup>) / 2</div>
<span class="t">التحويلات النقطية</span>
<p><b>الانسحاب:</b> <span class="m">z' = z + b</span> | <b>التشاابه / التحاكي:</b> <span class="m">z' - ω = k e<sup>iθ</sup> (z - ω)</span></p>
<p><b>الدوران:</b> <span class="m">z' - ω = e<sup>iθ</sup> (z - ω)</span></p>
</div></div></div>

<!-- المحطة 5: الهندسة في الفضاء -->
<div class="st k ca closed">
<div class="rl"><div class="nm">5</div></div>
<div class="cd">
<button class="hd" aria-expanded="false"><span class="tt"><b>الهندسة في الفضاء</b><small>الجداء السلمي، المستقيمات، والمستويات</small></span><span class="chev" aria-hidden="true">▾</span></button>
<div class="bd">
<span class="t">الجداء السلمي والتعامد</span>
<div class="f">u⃗ · v⃗ = xx' + yy' + zz' = ||u⃗||·||v⃗||·cos(θ)</div>
<p>تعامد مستقيمين أو مستويين يقتضي أن الجداء السلمي لأشعتهما الناظمة/الموجهة يساوي الصفر.</p>
<span class="t">تمثيل وسيطي لمستقيم ومستوي</span>
<div class="f">M(x,y,z) ∈ (D) ⟸ M = M<sub>0</sub> + t·u⃗</div>
<div class="f">ax + by + cz + d = 0 (معادلة ديكارتية لمستوي)</div>
<span class="t">المسافة بين نقطة ومستوي</span>
<div class="f">d(A, P) = |ax<sub>0</sub> + by<sub>0</sub> + cz<sub>0</sub> + d| / √(a<sup>2</sup> + b<sup>2</sup> + c<sup>2</sup>)</div>
</div></div></div>

<!-- المحطة 6: الاحتمالات -->
<div class="st k cg closed">
<div class="rl"><div class="nm">6</div></div>
<div class="cd">
<button class="hd" aria-expanded="false"><span class="tt"><b>الاحتمالات</b><small>التعداد، الاحتمال الشرطي، والمتغيرات العشوائية</small></span><span class="chev" aria-hidden="true">▾</span></button>
<div class="bd">
<span class="t">طرق التعداد الشهيرة</span>
<div class="f">القوائم: n<sup>p</sup> | الترتيبات: A<sub>n</sub><sup>p</sup> = n! / (n-p)! | التوفيقات: C<sub>n</sub><sup>p</sup> = n! / [p!(n-p)!]</div>
<span class="t">الاحتمال الشرطي</span>
<div class="f">P<sub>A</sub>(B) = P(A ∩ B) / P(A) , P(A) &gt; 0</div>
<p><b>دستور الاحتمالات الكلية:</b> <span class="m">P(B) = P(A ∩ B) + P(Ā ∩ B)</span></p>
<span class="t">المتغير العشوائي والامل الرياضياتي</span>
<div class="f">E(X) = Σ x<sub>i</sub> p<sub>i</sub> , V(X) = E(X<sup>2</sup>) - [E(X)]<sup>2</sup></div>
</div></div></div>

<!-- المحطة 7: المعادلات التفاضلية -->
<div class="st k cc closed">
<div class="rl"><div class="nm">7</div></div>
<div class="cd">
<button class="hd" aria-expanded="false"><span class="tt"><b>المعادلات التفاضلية</b><small>الحلول العامة والخاصة للشعب العلمية</small></span><span class="chev" aria-hidden="true">▾</span></button>
<div class="bd">
<span class="t">الشكل الأول y' = ay + b</span>
<div class="f">y(x) = C e<sup>ax</sup> - (b / a)  (حيث a ≠ 0)</div>
<p>الحل الخاص يتم إيجاده بتعويض الشرط الابتدائي المعطى (مثل <span class="m">y(0) = y<sub>0</sub></span>).</p>
<span class="t">الشكل الثاني y'' + ω<sup>2</sup>y = 0</span>
<div class="f">y(x) = A cos(ωx) + B sin(ωx)</div>
<p>حيث <span class="m">A</span> و <span class="m">B</span> ثوابت حقيقية تُعيّن بالشروط الابتدائية.</p>
</div></div></div>

<!-- محطة 8: الكويزات التفاعلية الشاملة -->
<div class="st k cz closed">
<div class="rl"><div class="nm">8</div></div>
<div class="cd">
<button class="hd" aria-expanded="false"><span class="tt"><b>محطة الكويزات الشاملة (جميع الوحدات)</b><small>اختبر معلوماتك من المبتدئ حتى مستوى البكالوريا</small></span><span class="chev" aria-hidden="true">▾</span></button>
<div class="bd">
<div class="qb">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
  <span class="tl">اختر المستوى:</span>
  <span style="font-weight:700;font-size:14px;color:var(--accent)">النقاط: <span id="qsp" dir="ltr">0</span></span>
</div>
<div style="display:flex;gap:6px;margin-bottom:12px;">
  <button class="level-btn active" data-level="beg">المبتدئ</button>
  <button class="level-btn" data-level="mid">المتوسط</button>
  <button class="level-btn" data-level="hard">البكالوريا</button>
</div>
<div id="quiz-box"></div>
<button id="qstart" class="mk" style="width:100%;margin-top:10px;">ابدأ كويز هذا المستوى</button>
<div id="qresult" style="display:none;margin-top:12px;padding:12px;border-radius:10px;background:var(--surface);border:1px solid var(--line);"></div>
</div>
</div></div></div>

<div class="st last k cy closed">
<div class="rl"><div class="nm">★</div></div>
<div class="cd">
<button class="hd" aria-expanded="false"><span class="tt"><b>نصائح البكالوريا الذهبية</b><small>قبل تسليم ورقة الإجابة</small></span><span class="chev" aria-hidden="true">▾</span></button>
<div class="bd">
<div class="s"><span class="n">1</span><div>قراءة الموضوع كاملة لمدة 10 دقائق وتخطيط وقت الإجابة بحكمة.</div></div>
<div class="s"><span class="n">2</span><div>كتابة القانون الأساسي بوضوح قبل الشروع في التعويض العددي.</div></div>
<div class="s"><span class="n">3</span><div>استخدام الوحدات والترميز الرياضي الصحيح ودقة الإشارة في الحسابات.</div></div>
<div class="s"><span class="n">4</span><div>التحقق من النتائج باستخدام الآلة الحاسبة أو الطرق البديلة كلما أمكن.</div></div>
</div></div></div>

<h2 class="sec">نماذج وتمارين مقترحة على نمط البكالوريا</h2>

<div class="ex">
<h3>التمرين الشامل: الدوال والمتتاليات والاحتمالات</h3>
<p>يحتوي اختبار البكالوريا عادة على 4 إلى 5 تمارين شاملة تغطي الدوال، الأعداد المركبة، المتتاليات، والهندسة في الفضاء.</p>
<ol>
<li>ابدأ دائماً بالتمارين الأقصر والأكثر ضماناً (الاحتمالات أو الأعداد المركبة البسيطة).</li>
<li>في مسائل الدوال، ركّز على إثبات وجود المستقيم المائل وحساب القيم الحدية بدقة.</li>
<li>في المتتاليات المرتبطة بدالة، اربط دائماً بين البرهان بالتراجع وتغيرات الدالة المرتبطة.</li>
</ol>
<details><summary>عرض نصائح الحل النموذجي</summary><div class="sol">
<p>التنظيم ووضوح الخطوات يمنحك العلامة الكاملة حتى وإن حدث خطأ حسابي بسيط في النهاية. دائماً اكتب جملة "بما أن الدالة مستمرة و..." قبل تطبيق مبرهنة القيم المتوسطة.</p>
</div></details>
</div>

<h2 class="sec">روابط ومراجع مقترحة للمراجعة</h2>
<div class="vd">
<div class="vh">قنوات أساتذة البكالوريا في الجزائر</div>
<a href="https://www.youtube.com/@noureddine2013" target="_blank" rel="noopener">قناة الأستاذ نور الدين في الرياضيات<small>شرح شامل لكافة وحدات البكالوريا من الألف إلى الياء</small></a>
<a href="https://www.youtube.com/@jouffre_math" target="_blank" rel="noopener">قناة الأستاذ جوفر (فرني عبد الجليل)<small>متتاليات ودوال وحوليات بكالوريا نموذجية</small></a>
</div>

<footer class="credit">
<p class="who">إعداد وتصميم: خبير البرمجيات والـ UI/UX - Okba</p>
<p>جميع الحقوق محفوظة © 2026</p>
<a class="ig" href="https://www.instagram.com/wgq.c?cplk=OHkyN2dja2tqNjE4" target="_blank" rel="noopener"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg><span>تابعني على انستغرام</span></a>
</footer>
</main>
<div id="toast" role="status" aria-live="polite"></div>
<script>
var sts=[].slice.call(document.querySelectorAll('.st'));
var K='bac-all-done',done={},total=sts.length-1;
try{done=JSON.parse(localStorage.getItem(K)||'{}')}catch(e){done={}}
function save(){try{localStorage.setItem(K,JSON.stringify(done))}catch(e){}}
function setOpen(s,o){s.classList.toggle('closed',!o);s.querySelector('.hd').setAttribute('aria-expanded',o?'true':'false')}
function paint(){
var c=0;
sts.forEach(function(s,i){
if(s.classList.contains('last'))return;
var d=!!done[i];if(d)c++;
s.querySelector('.nm').textContent=d?'✓':String(i+1);
var b=s.querySelector('.mk');
b.textContent=d?'تم الإتقان ✓':'أتقنت هذه المحطة';
b.setAttribute('aria-pressed',d?'true':'false');
});
document.getElementById('pt').textContent='أتقنت '+c+' من '+total+' محطات';
document.getElementById('pf').style.width=Math.round(c/total*100)+'%';
var nx=-1;
sts.forEach(function(s,i){s.classList.remove('next');if(nx<0&&!s.classList.contains('last')&&!done[i])nx=i});
if(nx>=0)sts[nx].classList.add('next');
document.getElementById('pm').textContent=c===0?'ابدأ بالمحطة 1: انطلاقة قوية نحو 20/20':c<3?'بداية رائعة، واصل تقدمك في الوحدات':c<6?'أنت تحقق إنجازاً مذهلاً، استمر':c<total?'اقتربت جداً من إنهاء كافة الوحدات':'أتممت كافة محطات البرنامج بنجاح تام!';
}
sts.forEach(function(s,i){
s.querySelector('.hd').addEventListener('click',function(){setOpen(s,s.classList.contains('closed'))});
if(!s.classList.contains('last')){
var b=document.createElement('button');
b.className='mk';
b.addEventListener('click',function(){
var was=!!done[i];done[i]=!was;save();paint();
if(!was){
var r=b.getBoundingClientRect();
var all=Object.keys(done).filter(function(k){return done[k]}).length===total;
burst(r.left+r.width/2,r.top+r.height/2,all?75:30);
toast(all?'مبروك! أتممت كافة محطات البرنامج، أنت جاهز للتميز':praise[Math.floor(Math.random()*praise.length)]);
var nm=s.querySelector('.nm');
if(!reduce&&nm.animate)nm.animate([{transform:'scale(1)'},{transform:'scale(1.35)'},{transform:'scale(1)'}],{duration:420,easing:'ease-out'});
}
});
s.querySelector('.bd').appendChild(b);
}
});
var allBtn=document.getElementById('all');
allBtn.addEventListener('click',function(){
var o=sts.some(function(s){return s.classList.contains('closed')});
sts.forEach(function(s){setOpen(s,o)});
allBtn.textContent=o?'طيّ الكل':'فتح الكل';
});
var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var cols=['#378ADD','#1D9E75','#D4537E','#7F77DD','#EF9F27','#D85A30','#639922','#C13584'];
var praise=['أحسنت! محطة جديدة في جعبتك','رائع، خطوة ثابتة نحو العلامة الكاملة','ممتاز، استمر بهذا النسق العالي','بطل! تفهم الوحدات بعمق'];
function burst(x,y,n){
if(reduce)return;
for(var k=0;k<n;k++){(function(k){
var p=document.createElement('i');
p.className='cf';p.style.left=x+'px';p.style.top=y+'px';p.style.background=cols[k%cols.length];
document.body.appendChild(p);
var a=Math.random()*6.283,d=70+Math.random()*140;
var an=p.animate([{transform:'translate(0,0) rotate(0deg)',opacity:1},{transform:'translate('+Math.cos(a)*d+'px,'+(Math.sin(a)*d+90)+'px) rotate('+Math.round(Math.random()*720)+'deg)',opacity:0}],{duration:950+Math.random()*500,easing:'cubic-bezier(.2,.7,.3,1)'});
an.onfinish=function(){p.remove()};
})(k)}
}
var tt;
function toast(m){var t=document.getElementById('toast');t.textContent=m;t.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){t.classList.remove('on')},2700)}
var mode='work',left=1500,iv=null,endAt=0;
var tg=document.getElementById('tg'),tr=document.getElementById('tr');
function fmt(n){var m=Math.floor(n/60),r=n%60;return (m<10?'0':'')+m+':'+(r<10?'0':'')+r}
function showT(){
document.getElementById('td').textContent=fmt(left);
document.getElementById('tl').textContent=mode==='work'?'وقت المراجعة':'وقت الاستراحة';
document.querySelector('.tm').classList.toggle('brk',mode!=='work');
}
function stopT(){clearInterval(iv);iv=null;tg.textContent='ابدأ'}
function tick(){
left=Math.max(0,Math.round((endAt-Date.now())/1000));
showT();
if(left>0)return;
stopT();
var r=tg.getBoundingClientRect();
if(mode==='work'){burst(r.left+r.width/2,r.top+r.height/2,40);toast('انتهت جلسة التركيز! خذ استراحة قصيرة');mode='break';left=300}
else{toast('انتهت الاستراحة، لنستأنف المراجعة');mode='work';left=1500}
try{if(navigator.vibrate)navigator.vibrate(200)}catch(e){}
showT();
}
tg.addEventListener('click',function(){
if(iv){clearInterval(iv);iv=null;tg.textContent='استئناف';return}
endAt=Date.now()+left*1000;
iv=setInterval(tick,500);
tg.textContent='إيقاف مؤقت';
});
tr.addEventListener('click',function(){stopT();mode='work';left=1500;showT()});
showT();

// نظام الكويزات الشامل لجميع الوحدات
var QK='bac-quiz-pts', qpts=0;
try{qpts=parseInt(localStorage.getItem(QK)||'0',10)||0}catch(e){qpts=0}

var quizData = {
  beg: [
    {q:"ما هي نهاية الدالة ln(x) لما x يؤول إلى +∞؟", o:["0", "1", "+∞", "−∞"], a: 2},
    {q:"ما هو القانون العام لمتتالية هندسية أساسها q؟", o:["u_n = u_0 · q^n", "u_n = u_0 + n·q", "u_{n+1} = u_n + q", "u_n = q^n / u_0"], a: 0},
    {q:"طويلة العدد المركب z = x + iy تُحسَب بالعلاقة:", o:["x + y", "√(x^2 + y^2)", "x^2 - y^2", "y / x"], a: 1},
    {q:"عدد التوفيقات C_n^p يعطى بالقانون:", o:["n! / (n-p)!", "n! / [p!(n-p)!]", "p! / n!", "n^p"], a: 1}
  ],
  mid: [
    {q:"دالة أصلية للدالة f(x) = e^{2x} هي:", o:["2e^{2x}", "(1/2)e^{2x}", "e^{2x} + C", "- (1/2)e^{2x}"], a: 1},
    {q:"حل المعادلة التفاضلية y' = 2y هو:", o:["y(x) = C e^{2x}", "y(x) = C e^{-2x}", "y(x) = 2x + C", "y(x) = C cos(2x)"], a: 0},
    {q:"الجداء السلمي لأشعة متعامدة في الفضاء يساوي:", o:["1", "-1", "0", "غير محدد"], a: 2},
    {q:"إذا كان الحادثان A و B مستقلين، فإن P(A ∩ B) يساوي:", o:["P(A) + P(B)", "P(A) · P(B)", "P(A) / P(B)", "0"], a: 1}
  ],
  hard: [
    {q:"إذا برهنا بالتقارب أن 0 ≤ u_n ≤ 3 وأن الدالة مرافقة مستمرة، فالنهاية l تحقق المعادلة:", o:["f(l) = l", "f(l) = 0", "f'(l) = 1", "l = 3"], a: 0},
    {q:"تحويل نقطي لاحقه z' = e^{iπ/2} (z - ω) + ω يمثل:", o:["انسحاب شعاعه ω", "دوران مركزه ω وزاويته π/2", "تحاكي نسبته i", "تناظر محورقي"], a: 1},
    {q:"تكامل ∫_0^1 x e^x dx يُحسب بالتجزئة فيساوي:", o:["1", "e - 1", "0", "e"], a: 0},
    {q:"دستور الاحتمالات الكلية لحدث B بدلالة الحادث A وحادثه العكسي Ā يُكتب:", o:["P(B) = P(A∩B) + P(Ā∩B)", "P(B) = P(A) + P(B)", "P(B) = P_A(B)", "P(B) = 1 - P(A)"], a: 0}
  ]
};

var currentLevel = 'beg';
var qi = 0, qansDone = false;
var qbox = document.getElementById('quiz-box'), qstart = document.getElementById('qstart'), qres = document.getElementById('qresult'), qsp = document.getElementById('qsp'), qpEl = document.getElementById('qp');

function renderQuiz(){
  var quiz = quizData[currentLevel];
  if(qi >= quiz.length){
    qbox.innerHTML = '';
    qstart.textContent = 'إعادة كويز هذا المستوى';
    qstart.disabled = false;
    qres.style.display = 'block';
    qres.innerHTML = '<div style="font-weight:700;text-align:center;margin-bottom:8px">أنهيت كويز هذا المستوى بنجاح! رصيدك الكلي: <span dir="ltr" style="font-size:20px;color:var(--accent)">'+qpts+'</span> نقطة</div>';
    return;
  }
  var Q = quiz[qi];
  var h = '<div class="qq">سؤال '+(qi+1)+' من '+quiz.length+': '+Q.q+'</div>';
  Q.o.forEach(function(opt, j){ h += '<button class="qa" data-i="'+j+'">'+opt+'</button>'; });
  qbox.innerHTML = h;
  qres.style.display = 'none';
  qansDone = false;
  qsp.textContent = qpts;
  if(qpEl) qpEl.textContent = 'نقاط الكويزات: '+qpts;
}

qbox.addEventListener('click', function(e){
  if(qansDone) return;
  var b = e.target.closest('.qa');
  if(!b) return;
  var idx = parseInt(b.getAttribute('data-i'), 10);
  qansDone = true;
  var quiz = quizData[currentLevel];
  var Q = quiz[qi], btns = qbox.querySelectorAll('.qa');
  btns.forEach(function(x){ x.disabled = true; });
  if(idx === Q.a){
    qpts += 10;
    b.classList.add('correct');
    qres.innerHTML = '<div class="qe" style="color:#0F6E56;font-weight:700">إجابة صحيحة! +10 نقاط.</div>';
    localStorage.setItem(QK, String(qpts));
  } else {
    b.classList.add('wrong');
    btns[Q.a].classList.add('correct');
    qres.innerHTML = '<div class="qe" style="color:#993C1D;font-weight:700">إجابة خاطئة. الإجابة الصحيحة: '+Q.o[Q.a]+'.</div>';
  }
  qres.style.display = 'block';
  qsp.textContent = qpts;
  if(qpEl) qpEl.textContent = 'نقاط الكويزات: '+qpts;
  setTimeout(function(){ qi++; renderQuiz(); }, 1400);
});

qstart.addEventListener('click', function(){
  qi = 0;
  qstart.textContent = 'السؤال التالي / إعادة';
  renderQuiz();
});

document.querySelectorAll('.level-btn').forEach(function(btn){
  btn.addEventListener('click', function(){
    document.querySelectorAll('.level-btn').forEach(function(b){ b.classList.remove('active'); });
    btn.classList.add('active');
    currentLevel = btn.getAttribute('data-level');
    qi = 0;
    qstart.textContent = 'ابدأ كويز هذا المستوى';
    qbox.innerHTML = '<p style="text-align:center;color:var(--text2);margin:10px 0;">اضغط على "ابدأ كويز هذا المستوى" لاختبار معلوماتك في مستوى ' + btn.textContent + '</p>';
    qres.style.display = 'none';
  });
});

if(qpEl) qpEl.textContent = 'نقاط الكويزات: '+qpts;
qsp.textContent = qpts;
qbox.innerHTML = '<p style="text-align:center;color:var(--text2);margin:10px 0;">اختر المستوى بالأعلى ثم اضغط ابدأ الكويز.</p>';

sts.forEach(function(s,k){s.style.animationDelay=(k*60)+'ms'});
paint();
</script>
</body>
</html>
"""

import os
with open("bac_math_masterpiece.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("File generated successfully: bac_math_masterpiece.html")