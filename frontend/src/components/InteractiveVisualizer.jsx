import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';

export const InteractiveVisualizer = () => {
    const svgRef = useRef(null);

    useEffect(() => {
        const width = window.innerWidth;
        const height = window.innerHeight;
        const svg = d3.select(svgRef.current)
            .attr('width', width)
            .attr('height', height);

        const particles = d3.range(80).map(() => ({
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 1.5,
            vy: (Math.random() - 0.5) * 1.5,
            r: Math.random() * 2 + 0.5
        }));

        const node = svg.selectAll('circle')
            .data(particles)
            .enter()
            .append('circle')
            .attr('r', d => d.r)
            .attr('fill', 'var(--accent-primary)')
            .attr('opacity', 0.25);

        const simulation = d3.forceSimulation(particles)
            .force('charge', d3.forceManyBody().strength(-2))
            .force('collision', d3.forceCollide().radius(d => d.r + 2))
            .on('tick', () => {
                node.attr('cx', d => d.x)
                    .attr('cy', d => d.y);

                // Wrap around screen
                particles.forEach(d => {
                    if (d.x < 0) d.x = width;
                    if (d.x > width) d.x = 0;
                    if (d.y < 0) d.y = height;
                    if (d.y > height) d.y = 0;
                });
            });

        // Global Mouse Interaction for ripples and particle physics
        const handleMouseMoveGlobal = (event) => {
            simulation.force('mouse', d3.forceRadial(150, event.clientX, event.clientY).strength(0.3));
            simulation.alphaTarget(0.1).restart();
        };

        const handleMouseDownGlobal = (event) => {
            const mx = event.clientX;
            const my = event.clientY;

            // Radial Pulse (Visual Beat)
            svg.append('circle')
                .attr('cx', mx)
                .attr('cy', my)
                .attr('r', 0)
                .attr('fill', 'none')
                .attr('stroke', 'var(--accent-primary)')
                .attr('stroke-width', 1)
                .attr('opacity', 0.5)
                .transition()
                .duration(1500)
                .ease(d3.easeExpOut)
                .attr('r', 400)
                .attr('opacity', 0)
                .remove();

            // Audio "Kick" effect on particles nearby
            particles.forEach(p => {
                const dx = p.x - mx;
                const dy = p.y - my;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 300) {
                    const power = (1 - dist / 300) * 15;
                    p.vx += (dx / dist) * power;
                    p.vy += (dy / dist) * power;
                }
            });
            simulation.alpha(0.8).restart();
        };

        window.addEventListener('mousemove', handleMouseMoveGlobal);
        window.addEventListener('mousedown', handleMouseDownGlobal);

        const handleResize = () => {
            const w = window.innerWidth;
            const h = window.innerHeight;
            svg.attr('width', w).attr('height', h);
            simulation.force('center', d3.forceCenter(w / 2, h / 2));
        };

        window.addEventListener('resize', handleResize);
        return () => {
            simulation.stop();
            window.removeEventListener('resize', handleResize);
            window.removeEventListener('mousemove', handleMouseMoveGlobal);
            window.removeEventListener('mousedown', handleMouseDownGlobal);
        };
    }, []);

    return (
        <svg
            ref={svgRef}
            style={{
                position: 'fixed',
                top: 0,
                left: 0,
                width: '100%',
                height: '100%',
                zIndex: -1,
                pointerEvents: 'none'
            }}
        />
    );
};
