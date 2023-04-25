from data.db_sess import global_init
import hotel_chain




def main():
    global_init("db/hotel_chain.sqlite")
    hotel_chain.main()


if __name__ == '__main__':
    main()
