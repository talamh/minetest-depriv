import sqlite3
import argparse
import os


def connect_to_database(db_path):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(db_path)
    return conn


def list_users(conn, privilege):
    """List users with a specific privilege in the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM auth WHERE id IN (SELECT id FROM user_privileges WHERE privilege = ?)",
                   (privilege,))
    users = cursor.fetchall()

    for user in users:
        print(user[0])

    print(f'{len(users)} players found in auth.sqlite with the {privilege} privilege')


def remove_privilege(conn, privilege):
    """Remove privilege for all users and return the count of affected players."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_privileges WHERE privilege = ?", (privilege,))
    count = cursor.rowcount  # Get the number of affected rows
    conn.commit()
    print(f"Privilege '{privilege}' removed for {count} players")
    return count


def main():
    parser = argparse.ArgumentParser(description='Manage users in SQLite database')
    parser.add_argument('-i', '--directory', metavar='directory', type=str, required=True,
                        help='Directory containing auth.sqlite')
    parser.add_argument('-r', '--remove', action='store_true', help='Remove privilege for all users')
    parser.add_argument('-p', '--privilege', metavar='privilege', type=str, required=True, help='Specify the privilege')
    args = parser.parse_args()

    db_path = os.path.join(args.directory, 'auth.sqlite')

    if not os.path.isfile(db_path):
        print(f"Error: auth.sqlite not found in directory '{args.directory}'")
        return

    conn = connect_to_database(db_path)

    if args.remove:
        removed_count = remove_privilege(conn, args.privilege)
        print(f"{removed_count} players had the {args.privilege} privilege removed.")
    else:
        list_users(conn, args.privilege)

    conn.close()


if __name__ == "__main__":
    main()
