import streamlit as st

def render_header():
    st.markdown("### Recirculating Photonic Integrated Circuits for Machine Learning  \n"
                "MSc Thesis, **Mateusz Mazurkiewicz**")

    with st.container(border=True):
        st.image("assets/diagram_time_delay.png", caption="The circuit modelled using temporal coupled mode theory.")

        with st.expander("Temporal Coupled Mode Theory", expanded=False):
            st.markdown(
                "[*Photonic Crystals: Molding the Flow of Light*](http://ab-initio.mit.edu/book/) textbook models the coupling between: a resonant optical cavity with a single stationary mode of amplitude $A$, and propagating eigenmodes $s_{\\pm}$ in adjacent waveguides, by:")

            st.latex(r'''
             \frac{dA}{dt} = (-i \omega_0 - \frac{\kappa_x}{2} - \frac{m \kappa_w}{2}) A + \sum_{m,+} \sqrt{\kappa_w} s_{m,+}
             ''')

            st.markdown(
                r'where $m$ is the number of coupled propagating modes ($_{m,+}$ specifically for inputs to the cavity), $\kappa_w$ is a decay constant for waveguide-cavity coupling, and $\omega_0$ is natural frequency of resonant cavity. $\kappa_x$ is the sum of radiative, absorption, and other losses, and for the coupled modes:')

            st.latex(r'''
             s_{l_1\pm} = \pm s_{l_2\pm} + \sqrt{\kappa_w}A
             ''')

            st.markdown("depending on circuit layout. More generally, [*Temporal Coupled-Mode Theory and the Presence of Non-Orthogonal Modes in Lossless Multimode Cavities*](https://web.stanford.edu/group/fan/publication/Suh_IEEEJQE_40_1511_2004.pdf) paper presents a formal description of a multimode cavity with $m$ ports,")
            _, centered, _ = st.columns([1,2,1])
            with centered:
                st.image("assets/paper_img.png", width=300)
            st.markdown("with $a$ being an $n$-element amplitude vector for cavity modes, such that $|a_i|^2$ is energy in the $i$th optical mode, with $| s_+ \\rangle$ an $m$-element vector of amplitudes of incoming propagating modes, and similarily $| s_- \\rangle$ for outgoing, the equations describing system dynamics are:")

            st.latex(r'''
             \frac{da}{dt} = (i \Omega - \Gamma) a + K^T | s_+ \rangle
             ''')

            st.latex(r'''
             | s_- \rangle = C | s_+ \rangle + D a
             ''')

            st.markdown("Where $\Omega$ is an $n$ by $n$ matrix, whose diagonal entries are natural frequencies of the $n$ resonant modes, and off-diagonal entries represent coupling between them, $\Gamma$ contains the decay constants, $K = D$ are the coupling matrices, and $C$ is the scattering matrix.")
            st.markdown("We also have $D^{+}D = 2 \Gamma$ and $CD^{*} = -D$, the former derived from energy conservation, and latter from time reversal equivalence.")

        with st.expander("System dynamics of the circuit (I)", expanded=False):

            st.markdown("The propagating modes in waveguides are related to each other, and to modes in cavities, as follows:")

            st.latex(r'''
            s_{1+}(t) = f(t) \qquad \text{(forcing function)}
            ''')

            st.latex(r'''
            s_{2+}(t) = s_{1+}(t) + \sqrt{\kappa_{w, 1}}A_1(t)
            ''')

            st.latex(r'''
            s_{3+}(t) = s_{2+}(t-t_{\text{delay}})
            ''')

            st.latex(r'''
            s_{3-}(t) = - s_{3+}(t) + \sqrt{\kappa_{w, 2}}A_2(t)
            ''')

            st.latex(r'''
            s_{2-}(t) = s_{3-}(t-t_{\text{delay}})
            ''')

            st.latex(r'''
            s_{1-}(t) = s_{2-}(t) + \sqrt{\kappa_{w, 1}}A_1(t)
            ''')

            st.markdown("While the cavity dynamics are described by:")

            st.latex(r'''
                        \frac{dA_1}{dt}(t) = (-i \omega_1 - \frac{\kappa_{x, 1}}{2} - \kappa_{w, 1}) A_1(t) + \sqrt{\kappa_{w, 1}} (s_{1+}(t) + s_{2-}(t))
                        ''')

            st.latex(r'''
                        \frac{dA_2}{dt}(t) = (-i \omega_2 - \frac{\kappa_{x, 2}}{2} - \frac{\kappa_{w, 2}}{2}) A_2(t) + \sqrt{\kappa_{w, 2}} s_{3+}(t)
                        ''')

        with st.expander("System dynamics of the circuit (II)", expanded=False):
            st.markdown("By elimination by substitution, we obtain")

            st.latex(r'''
                        s_{1+}(t) = f(t) \qquad \text{(forcing function)}
                        ''')

            st.latex(r'''
                        s_{2+}(t) = f(t) + \sqrt{\kappa_{w, 1}}A_1(t)
                        ''')

            st.latex(r'''
                        s_{3+}(t) = f(t-t_{\text{delay}}) + \sqrt{\kappa_{w, 1}}A_1(t-t_{\text{delay}})
                        ''')

            st.latex(r'''
                        s_{3-}(t) = - f(t-t_{\text{delay}}) - \sqrt{\kappa_{w, 1}}A_1(t-t_{\text{delay}}) + \sqrt{\kappa_{w, 2}}A_2(t)
                        ''')

            st.latex(r'''
                        s_{2-}(t) = - f(t-2t_{\text{delay}}) - \sqrt{\kappa_{w, 1}}A_1(t-2t_{\text{delay}}) + \sqrt{\kappa_{w, 2}}A_2(t-t_{\text{delay}})
                        ''')

            st.latex(r'''
                \begin{aligned}
                        s_{1-}(t) &= - f(t-2t_{\text{delay}}) - \sqrt{\kappa_{w, 1}}A_1(t-2t_{\text{delay}}) + \sqrt{\kappa_{w, 2}}A_2(t-t_{\text{delay}}) \\
                        &\quad + \sqrt{\kappa_{w, 1}}A_1(t)
                \end{aligned}
                        ''')

            st.latex(r'''
                \begin{aligned}
                    \frac{dA_1}{dt}(t) &= (-i \omega_1 - \frac{\kappa_{x, 1}}{2} - \kappa_{w, 1}) A_1(t) + \sqrt{\kappa_{w, 1}} (f(t) - f(t-2t_{\text{delay}}) \\
                    &\quad - \sqrt{\kappa_{w, 1}}A_1(t-2t_{\text{delay}}) + \sqrt{\kappa_{w, 2}}A_2(t-t_{\text{delay}}))
                \end{aligned}
                    ''')

            st.latex(r'''
                \begin{aligned}
                    \frac{dA_2}{dt}(t) &= (-i \omega_2 - \frac{\kappa_{x, 2}}{2} - \frac{\kappa_{w, 2}}{2}) A_2(t) + \sqrt{\kappa_{w, 2}} (f(t-t_{\text{delay}}) \\
                    &\quad + \sqrt{\kappa_{w, 1}}A_1(t-t_{\text{delay}}))
                \end{aligned}
                    ''')

        with st.expander("Verifying the model (resonant cavities)", expanded=False):
            st.markdown("First cavity:")

            st.latex(r'''
                        \frac{dA_1}{dt}(t) = (-i \omega_1 - \frac{\kappa_{x, 1}}{2} - \kappa_{w, 1}) A_1(t) + \sqrt{\kappa_{w, 1}} (s_{1+}(t) + s_{2-}(t))
                        ''')

            st.markdown("$K = D$: both diagonal entries of both matrices are $\sqrt{\kappa_{w, 1}}$, satisfied.")
            st.markdown("$D^{+} D = 2 \Gamma$: $2 \sqrt{\kappa_{w, 1}}^2 = 2\kappa_{w, 1}$, satisfied.")
            st.markdown("$CD^{*} = -D$: **TBD**.")

            st.markdown("Second cavity:")

            st.latex(r'''
                        \frac{dA_2}{dt}(t) = (-i \omega_2 - \frac{\kappa_{x, 2}}{2} - \frac{\kappa_{w, 2}}{2}) A_2(t) + \sqrt{\kappa_{w, 2}} s_{3+}(t)
                        ''')

            st.markdown("$K = D$: $\sqrt{\kappa_{w, 2}}=\sqrt{\kappa_{w, 2}}$, satisfied.")
            st.markdown("$D^{+} D = 2 \Gamma$: $\sqrt{\kappa_{w, 2}}^2 = 2\\frac{\kappa_{w, 1}}{2}$ satisfied.")
            st.markdown("$CD^{*} = -D$: $-1 \cdot \sqrt{\kappa_{w, 2}} = - \sqrt{\kappa_{w, 2}}$, satisfied.")

        #with st.expander("Verifying the model (conservation of energy)", expanded=False):
        #    st.markdown(r"""
        #    For any $\tau$, the following must hold: $\int_0^{\tau} |s_{1+}(t)|^2 dt \geq |A_1(\tau)|^2 + |A_2(\tau)|^2 - \int_0^{\tau} |s_{1-}(t)|^2 dt$,
        #    or, in other words, total energy delivered to the system must be greater or equal to the sum of energies in cavities and energy that left the circuit.
        #    """)