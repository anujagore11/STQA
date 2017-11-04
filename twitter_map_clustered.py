from argparse import ArgumentParser
import folium
import json

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--geojson')
    parser.add_argument('--map')
    return parser


def make_map(geojson_file, map_file):
    tweet_map = folium.Map(location=[50, 5],
                           zoom_start=5)
    marker_cluster = folium.MarkerCluster().add_to(tweet_map)
    geodata =json.load(open(geojson_file))
    for tweet in geodata['features']:
       print("***",tweet)
       tweet['geometry']['coordinates'].reverse()
       marker = folium.Marker(tweet['geometry']['coordinates'], popup = tweet['properties']['text'])
   # geojson_layer = folium.GeoJson(open(geojson_file),
                                   #name='geojson')
       marker.add_to(marker_cluster)
    tweet_map.save(map_file)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    make_map(args.geojson, args.map)
