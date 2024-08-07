import { List, Avatar, Typography } from "@telegram-apps/telegram-ui";

interface User {
    id: number;
    telegram_id: number;
    fullname: string;
    joined_at: string;
    is_banned: boolean;
    points: number;
}

const UsersPage: React.FC = () => {
    const [users, setUsers] = useState<User[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get('https://example.com/api/users')
            .then(response => {
                setUsers(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    const rankedUsers = users.sort((a, b) => b.points - a.points);

    return (
        <div>
            <Typography variant="h4" component="h1">
                Users Ranking
            </Typography>
            <List>
                {rankedUsers.map((user, index) => (
                    <ListItem key={user.id}>
                        <ListItemAvatar>
                            <Avatar src={``} />
                        </ListItemAvatar>
                        <ListItemText
                            primary={user.fullname}
                            secondary={`Points: ${user.points}`}
                        />
                    </ListItem>
                ))}
            </List>
            {loading && <Typography variant="body1">Loading...</Typography>}
        </div>
    );
};

export default UsersPage;