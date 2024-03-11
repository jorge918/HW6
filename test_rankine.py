

from rankine import Rankine

def main():
    # Case i
    print("Case i:")
    rankine_i = Rankine(p_high=8000, p_low=8)
    efficiency_i = rankine_i.calc_efficiency()
    rankine_i.print_summary()
    print("Efficiency:", efficiency_i)

    # Case ii
    print("\nCase ii:")
    rankine_ii = Rankine(p_high=8000, p_low=8, t_high=1.7*rankine_i.state1.T)
    efficiency_ii = rankine_ii.calc_efficiency()
    rankine_ii.print_summary()
    print("Efficiency:", efficiency_ii)

if __name__ == "__main__":
    main()
