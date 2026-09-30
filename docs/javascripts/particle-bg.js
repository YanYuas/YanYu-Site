// ============================================================
// particle-bg.js · 首页粒子星空背景
// ============================================================
// 功能：
//   1. Canvas 全屏粒子星空（深蓝底 + 白/金粒子）
//   2. 粒子之间距离近时画连接线（星座效果）
//   3. 鼠标移动时，附近粒子被轻微吸引
//   4. 偶尔有流星划过
//   5. 只在首页生效（检测 body 上的特定 class）
// ============================================================

(function () {
  'use strict';

  // 只在首页运行：首页有 .home 容器
  const homeEl = document.querySelector('.home');
  if (!homeEl) return;

  // ---------- 创建 Canvas ----------
  // 挂到 .home 内部，而不是 body —— 因为 .home 有 z-index:1 创建了层叠上下文，
  // 挂在 body 上的 canvas 会被整个 .home（包括背景图）盖住。
  const canvas = document.createElement('canvas');
  canvas.id = 'particle-canvas';
  canvas.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    pointer-events: none;
  `;
  homeEl.appendChild(canvas);

  const ctx = canvas.getContext('2d');
  let W, H;

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  // ---------- 粒子配置 ----------
  // 有背景图了，粒子做点缀就行，不要太多太亮，否则和背景图抢戏
  const PARTICLE_COUNT = Math.min(70, Math.floor(W * H / 18000)); // 粒子数量（少而精）
  const CONNECT_DIST = 100;   // 粒子之间距离小于这个值时连线（缩短，减少连线）
  const MOUSE_RADIUS = 150;   // 鼠标影响半径
  const STAR_COLORS = [
    'rgba(255, 250, 235, ',   // 暖白星（最主要，和金色背景区分）
    'rgba(255, 250, 235, ',
    'rgba(255, 245, 220, ',   // 浅暖白
    'rgba(255, 230, 180, ',   // 淡金星（点缀）
    'rgba(255, 215, 150, ',   // 金色（少量）
  ];

  // ---------- 粒子类 ----------
  class Particle {
    constructor() {
      this.reset();
    }

    reset() {
      this.x = Math.random() * W;
      this.y = Math.random() * H;
      this.vx = (Math.random() - 0.5) * 0.25; // 水平速度（更慢）
      this.vy = (Math.random() - 0.5) * 0.25; // 垂直速度
      this.radius = Math.random() * 1.5 + 0.4; // 粒子大小（更小更柔和）
      this.color = STAR_COLORS[Math.floor(Math.random() * STAR_COLORS.length)];
      this.baseAlpha = Math.random() * 0.35 + 0.15; // 基础透明度（更暗，做点缀）
      this.alpha = this.baseAlpha;
      this.twinkleSpeed = Math.random() * 0.015 + 0.005; // 闪烁速度（更慢）
      this.twinklePhase = Math.random() * Math.PI * 2;    // 闪烁相位
    }

    update(mouse) {
      // 缓慢移动
      this.x += this.vx;
      this.y += this.vy;

      // 边界环绕（从一边出去从另一边进来）
      if (this.x < -10) this.x = W + 10;
      if (this.x > W + 10) this.x = -10;
      if (this.y < -10) this.y = H + 10;
      if (this.y > H + 10) this.y = -10;

      // 鼠标吸引效果
      if (mouse.active) {
        const dx = mouse.x - this.x;
        const dy = mouse.y - this.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < MOUSE_RADIUS && dist > 0) {
          const force = (MOUSE_RADIUS - dist) / MOUSE_RADIUS * 0.015;
          this.vx += (dx / dist) * force;
          this.vy += (dy / dist) * force;
          // 靠近鼠标时变亮
          this.alpha = Math.min(1, this.baseAlpha + (1 - dist / MOUSE_RADIUS) * 0.5);
        } else {
          this.alpha = this.baseAlpha;
        }
      }

      // 速度衰减（防止越飞越快）
      this.vx *= 0.99;
      this.vy *= 0.99;

      // 闪烁效果
      this.twinklePhase += this.twinkleSpeed;
      const twinkle = Math.sin(this.twinklePhase) * 0.3 + 0.7;
      this.currentAlpha = this.alpha * twinkle;
    }

    draw() {
      // 外层光晕（柔和）
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius * 3, 0, Math.PI * 2);
      ctx.fillStyle = this.color + (this.currentAlpha * 0.08) + ')';
      ctx.fill();

      // 粒子核心
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fillStyle = this.color + this.currentAlpha + ')';
      ctx.fill();
    }
  }

  // ---------- 流星类 ----------
  class Meteor {
    constructor() {
      this.reset();
    }

    reset() {
      this.x = Math.random() * W * 0.8;
      this.y = Math.random() * H * 0.3 - 50;
      this.length = Math.random() * 80 + 60;
      this.speed = Math.random() * 8 + 6;
      this.angle = Math.PI / 4 + (Math.random() - 0.5) * 0.3; // 大约45度
      this.active = false;
      this.life = 0;
      this.maxLife = Math.random() * 60 + 40;
    }

    activate() {
      this.reset();
      this.active = true;
      this.life = 0;
    }

    update() {
      if (!this.active) return;
      this.x += Math.cos(this.angle) * this.speed;
      this.y += Math.sin(this.angle) * this.speed;
      this.life++;
      if (this.life > this.maxLife || this.x > W + 100 || this.y > H + 100) {
        this.active = false;
      }
    }

    draw() {
      if (!this.active) return;
      const tailX = this.x - Math.cos(this.angle) * this.length;
      const tailY = this.y - Math.sin(this.angle) * this.length;
      const alpha = 1 - this.life / this.maxLife;

      const gradient = ctx.createLinearGradient(this.x, this.y, tailX, tailY);
      gradient.addColorStop(0, `rgba(255, 230, 180, ${alpha})`);
      gradient.addColorStop(0.3, `rgba(255, 200, 130, ${alpha * 0.6})`);
      gradient.addColorStop(1, 'rgba(255, 200, 130, 0)');

      ctx.beginPath();
      ctx.moveTo(this.x, this.y);
      ctx.lineTo(tailX, tailY);
      ctx.strokeStyle = gradient;
      ctx.lineWidth = 2;
      ctx.lineCap = 'round';
      ctx.stroke();

      // 流星头部光点
      ctx.beginPath();
      ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, 240, 200, ${alpha})`;
      ctx.fill();
    }
  }

  // ---------- 初始化粒子 ----------
  const particles = [];
  for (let i = 0; i < PARTICLE_COUNT; i++) {
    particles.push(new Particle());
  }

  // ---------- 初始化流星 ----------
  // 流星要稀有，偶尔划过才有感觉，太多就乱了
  const meteors = [];
  for (let i = 0; i < 2; i++) {
    meteors.push(new Meteor());
  }
  let meteorTimer = 0;
  const METEOR_INTERVAL = 600; // 大约每10秒一颗（60fps * 10 = 600帧）

  // ---------- 鼠标状态 ----------
  const mouse = { x: 0, y: 0, active: false };
  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    mouse.active = true;
  });
  window.addEventListener('mouseout', () => {
    mouse.active = false;
  });

  // ---------- 画连接线 ----------
  function drawConnections() {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < CONNECT_DIST) {
          const alpha = (1 - dist / CONNECT_DIST) * 0.08;  // 连接线更淡
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(255, 210, 140, ${alpha})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    }
  }

  // ---------- 主循环 ----------
  function animate() {
    // 用 destination-out 模式擦除，产生拖尾效果
    // 关键：不能用 fillStyle 半透明覆盖，那会在透明 canvas 上累积深色，盖住背景图
    // destination-out 只降低已有像素的透明度，不增加任何颜色
    ctx.globalCompositeOperation = 'destination-out';
    ctx.fillStyle = 'rgba(0, 0, 0, 0.08)';  // 每帧擦除8%，拖尾长度适中
    ctx.fillRect(0, 0, W, H);
    ctx.globalCompositeOperation = 'source-over';  // 切回正常模式画粒子

    // 更新和绘制粒子
    for (const p of particles) {
      p.update(mouse);
      p.draw();
    }

    // 画连接线
    drawConnections();

    // 流星
    meteorTimer++;
    if (meteorTimer > METEOR_INTERVAL) {
      meteorTimer = 0;
      const inactiveMeteor = meteors.find(m => !m.active);
      if (inactiveMeteor) inactiveMeteor.activate();
    }
    for (const m of meteors) {
      m.update();
      m.draw();
    }

    requestAnimationFrame(animate);
  }

  // 初始清空（透明背景，露出背景图）
  ctx.clearRect(0, 0, W, H);

  animate();

  // ============================================================
  // 打字机效果
  // ============================================================
  // 给首页的名字和副标题加上逐字打出效果
  // ============================================================

  function typeWriter(element, text, speed, callback) {
    let i = 0;
    element.textContent = '';
    function type() {
      if (i < text.length) {
        element.textContent += text.charAt(i);
        i++;
        setTimeout(type, speed);
      } else if (callback) {
        callback();
      }
    }
    type();
  }

  // 等待页面加载完成
  window.addEventListener('load', () => {
    const heroTitle = document.querySelector('.hero h1');
    const heroSubtitle = document.querySelector('.hero .hero-subtitle');
    const heroButtons = document.querySelector('.hero .hero-buttons');

    if (heroTitle) {
      const nameText = heroTitle.textContent;
      // 延迟一点开始，让粒子先动起来
      setTimeout(() => {
        // 名字打字机
        typeWriter(heroTitle, nameText, 180, () => {
          // 名字打完后，副标题开始打字机
          if (heroSubtitle) {
            const subtitleText = heroSubtitle.textContent;
            heroSubtitle.style.opacity = '1';
            heroSubtitle.classList.add('typing');  // 加光标
            typeWriter(heroSubtitle, subtitleText, 60, () => {
              // 副标题打完后，移除光标，按钮淡入
              setTimeout(() => {
                heroSubtitle.classList.remove('typing');
              }, 1500);
              if (heroButtons) {
                heroButtons.style.animation = 'none';
                heroButtons.style.opacity = '0';
                setTimeout(() => {
                  heroButtons.style.animation = 'buttonsFadeIn 1s ease forwards';
                }, 50);
              }
            });
          }
        });
      }, 800);
    }
  });

})();
